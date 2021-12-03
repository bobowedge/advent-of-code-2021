def parse(path):
    output = []
    with open(path) as data:
        for line in data:
            line = line.split()
            direction = line[0]
            distance = int(line[1])
            output.append((direction, distance))
    return output

def part1(data):
    horizontal = 0
    depth = 0
    for direction, distance in data:
        if direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
        else:
            horizontal += distance
    return horizontal * depth

def part2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for direction, distance in data:
        if direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        else:
            horizontal += distance
            depth += aim * distance
    return horizontal * depth

data = parse("data/day02.txt")
print(f"Solution 1: {part1(data)}")
print(f"Solution 2: {part2(data)}")

