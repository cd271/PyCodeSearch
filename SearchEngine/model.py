import torch
from unixcoder import UniXcoder
from torch.nn import CosineSimilarity

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
code_search_model = UniXcoder("Lazyhope/unixcoder-nine-advtest")
code_search_model.to(device)
clone_detection_model = UniXcoder("Lazyhope/unixcoder-clone-detection")
clone_detection_model.to(device)

def get_code_embeddings(code, model):
    tokens_ids = model.tokenize([code], max_length=512, mode="<encoder-only>")
    source_ids = torch.tensor(tokens_ids).to(device)
    _, embeddings = model(source_ids)

    return embeddings

def get_cos_similarity(query_embedding, code_embedding):
    cosine_sim = CosineSimilarity(dim=1, eps=1e-8)
    return cosine_sim(query_embedding, code_embedding)

def retrieve_topN(repo_info, similarities, n):
    # Convert similarities tensor to a list
    similarities_list = similarities.tolist()
    
    # Combine functions with cosine similarities
    func_similarities = list(zip(repo_info["funcs"], similarities_list))
    
    # Sort the func_similarities list based on cosine similarities
    sorted_similarities = sorted(func_similarities, key=lambda x: x[1], reverse=True)
    most_similar_funcs = sorted_similarities[:n]
    
    # Extract the function names from the most_similar_funcs list
    similar_func_names = [func for func, _ in most_similar_funcs]
    
    return similar_func_names