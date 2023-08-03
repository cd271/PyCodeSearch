from search_engine.unixcoder import UniXcoder
import torch
from torch.nn import CosineSimilarity
from tqdm import tqdm

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
code_search_model = UniXcoder("Lazyhope/unixcoder-nine-advtest")
code_search_model.to(device)

def get_code_embeddings(code, model):
    tokens_ids = model.tokenize([code], max_length=512, mode="<encoder-only>")
    source_ids = torch.tensor(tokens_ids).to(device)
    _, embeddings = model(source_ids)

    return embeddings

def get_cos_similarity(query_embedding, code_embedding):
    cosine_sim = CosineSimilarity(dim=1, eps=1e-8)
    return cosine_sim(query_embedding, code_embedding)

def retrieve_topN(repo_info, similarities, n):
    similarities_list = similarities.tolist()
    func_similarities = list(zip(repo_info["funcs"], similarities_list))
    
    sorted_similarities = sorted(func_similarities, key=lambda x: x[1], reverse=True)
    most_similar_funcs = sorted_similarities[:n]
    
    similar_func_names = [func for func, _ in most_similar_funcs]
    
    return similar_func_names


class Code2CodeSearchEngine:
    def __init__(self, repo_info):
        self.repo_info = repo_info
        self.code_embeddings = self.compute_code_embeddings()

    def compute_code_embeddings(self):
        code_embeddings = []
        print("Generating code embeddings for dataset ... ")
        for func in tqdm(self.repo_info["funcs"]):
            code_embeddings.append(get_code_embeddings(func, code_search_model))
        print("Dataset code embeddings generated!")
        return code_embeddings

    def search(self, query, n):
        input_embedding = get_code_embeddings(query, code_search_model)
        similarities = get_cos_similarity(input_embedding, torch.stack(self.code_embeddings))
        similar_func_names = retrieve_topN(self.repo_info, similarities, n)

        print(f'The most similar {n} code snippets:')
        for func_name in similar_func_names:
            print(f'\n------------------------------------------------------------------\n {func_name}')


class Text2CodeSearchEngine:
    def __init__(self, repo_info):
        self.repo_info = repo_info
        self.code_embeddings = self.compute_code_embeddings()

    def compute_code_embeddings(self):
        code_embeddings = []
        print("Generating code embeddings for dataset ... ")
        for func in tqdm(self.repo_info["funcs"]):
            code_embeddings.append(get_code_embeddings(func, code_search_model))
        print("Dataset code embeddings generated!")
        
        code_embeddings = torch.stack([torch.tensor(embedding) for embedding in code_embeddings])
        return torch.squeeze(code_embeddings)

    def search(self, query, n):
        input_embedding = get_code_embeddings(query, code_search_model)
        similarities = get_cos_similarity(input_embedding, self.code_embeddings)
        similar_func_names = retrieve_topN(self.repo_info, similarities, n)

        print(f'The most similar {n} code snippets:')
        for func_name in similar_func_names:
            print(f'\n------------------------------------------------------------------\n {func_name}')