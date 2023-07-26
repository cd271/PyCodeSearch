import json

def funcs_to_lists(funcs, func_codes, docs):
    for func_name, func_info in funcs.items():
        if func_info.get("source_code") is not None:
            func_codes.append(func_info["source_code"])
        if func_info.get("doc") is None:
            continue
        for key in ["full", "long_description", "short_description"]:
            if func_info["doc"].get(key) is not None:
                docs.append(f"{func_name} {func_info['doc'].get(key)}")
                break

def file_to_lists(filename):
    func_codes = []
    docs = []
    with open(filename, "r") as f:
        dic = json.load(f)
    dic.pop("readme_files", None)
    for dir_name, files in dic.items():
        for file in files:
            if file.get("functions") is not None:
                funcs_to_lists(file["functions"], func_codes, docs)
            if file.get("classes") is not None:
                for class_name, class_info in file["classes"].items():
                    if class_info.get("methods") is not None:
                        funcs_to_lists(class_info["methods"], func_codes, docs)
    return func_codes