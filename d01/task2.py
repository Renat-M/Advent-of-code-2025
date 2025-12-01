from task1 import parse_line
from utils import read_from_file as r

def task2(file_path):
    lines = r.read_file(file_path)
    instructions = parse_line(lines)

    position = 50
    count = 0
    for direction, value in instructions:
        for _ in range(value):
            if direction == 'L':
                position -= 1
            elif direction == 'R':
                position += 1
            if position == -1 or position == 100:
                position %= 100
            if position == 0:
                count += 1
    return count

if __name__ == "__main__":
    print(task2('input.txt'))