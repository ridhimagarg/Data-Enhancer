import json

def read_json(json_file_path: str):
    with open(json_file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data

def save_json(path_to_save_json: str, data):
    with open(path_to_save_json, 'w') as file:
        json.dump(data, file, indent=4)

def read_txt(path_to_txt_file:str):
    with open(path_to_txt_file, 'r', encoding="utf8") as txt:
        data = txt.read()

    return data

def save_txt(path_to_txt_file:str, data):
    with open(path_to_txt_file, 'w', encoding="utf8") as file:
        file.write(data)       