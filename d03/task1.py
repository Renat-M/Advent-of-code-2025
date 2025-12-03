from utils import read_from_file as r

def find_max_num(line):
    len_str = len(line)
    max_num = 0

    for i in range(len_str):
        for j in range(i + 1, len_str):
            num = 10 * int(line[i]) + int(line[j])
            if num > max_num:
                max_num = num
    return max_num

def task1(file_path):
    input_data = r.read_file(file_path)
    res = 0
    for line in input_data:
        res += find_max_num(line)
    return res

if __name__ == "__main__":
    print(task1("input.txt"))