from utils import read_from_file as r

def task1(file_path):
    lines = r.read_file(file_path)

    input_data = lines[0].split(',')
    res = 0
    for id_range in input_data:
        int_id_range = [int(x) for x in id_range.split('-')]
        for id in range(int_id_range[0], int_id_range[1] + 1):
            id_str = str(id)
            if len(id_str) % 2 == 0:
                if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
                    res += id
    return res

if __name__ == "__main__":
    print(task1('input.txt'))