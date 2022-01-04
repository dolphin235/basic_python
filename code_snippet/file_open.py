
def write_str(file_path, input_str):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(input_str)

def read_str(file_path):
    with open(file_path, 'rb', encoding='utf-8') as f:
        text = f.read()
    return text

def read_str_to_list(file_path):
    text_list = list()
    with open(file_path, 'rb', encoding='utf-8') as f:
        text_list = f.readlines()
    return text_list
