from utils import read_from_file as r

def find_max_num(line):
    to_remove = len(line) - 12
    max_num = []
    for char in line:
        while to_remove > 0 and max_num and max_num[-1] < char:
            max_num.pop()
            to_remove -= 1
        max_num.append(char)
    return int("".join(max_num[:12]))

def task2(file_path):
    input_data = r.read_file(file_path)
    res = 0
    for line in input_data:
        res += find_max_num(line)
    return res

if __name__ == "__main__":
    print(task2("input.txt"))