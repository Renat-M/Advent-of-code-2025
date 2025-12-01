def read_file(file_path):
    with open(file_path, 'r') as file:
        content = [line.strip() for line in file.readlines()]
    return content
