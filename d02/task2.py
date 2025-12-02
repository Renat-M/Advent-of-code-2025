from utils import read_from_file as r

def is_invalid(id_str):
    len_str = len(id_str)
    for chunk_size in range(1, len_str // 2 + 1):
        if len_str % chunk_size != 0:
            continue
        repeat = len_str // chunk_size
        if repeat < 2:
            continue
        chunk = id_str[:chunk_size]
        if chunk * repeat == id_str:
            return True
    return False

def task2(file_path):
    lines = r.read_file(file_path)

    input_data = lines[0].split(',')
    res = 0
    for id_range in input_data:
        int_id_range = [int(x) for x in id_range.split('-')]
        for id in range(int_id_range[0], int_id_range[1] + 1):
            if is_invalid(str(id)):
                res += id
    return res

if __name__ == "__main__":
    print(task2('input.txt'))