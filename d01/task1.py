from utils import read_from_file as r

def parse_line(lines):
    return [(line[0], int(line[1:])) for line in lines]

def task1(file_path):
    lines = r.read_file(file_path)
    instructions = parse_line(lines)

    position = 50
    count = 0
    for direction, value in instructions:
        if direction == 'L':
            position = (position - value) % 100
        elif direction == 'R':
            position = (position + value) % 100
        if position == 0:
            count += 1
    return count

if __name__ == "__main__":
    print(task1('input.txt'))
