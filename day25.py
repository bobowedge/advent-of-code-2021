data = open("data/day25.txt").read().splitlines()

data = [[c for c in line] for line in data]

def move_east(data):
    new_data = [[c for c in line] for line in data]
    for row,line in enumerate(data):
        for col,c in enumerate(line):
            if c == ">":
                ecol = (col + 1) % len(line)
                if line[ecol] == ".":
                    new_data[row][col] = "."
                    new_data[row][ecol] = ">"
    return new_data

def move_south(data):
    new_data = [[c for c in line] for line in data]
    for row,line in enumerate(data):
        erow = (row + 1) % len(data)
        for col,c in enumerate(line):
            if c == "v" and data[erow][col] == ".":
                new_data[row][col] = "."
                new_data[erow][col] = "v"
    return new_data

def solution1(data):
    steps = 0
    new_data = None
    while True:
        new_data = move_east(data)
        new_data = move_south(new_data)
        steps += 1
        if new_data == data:
            break
        data = new_data
    return steps 

print(solution1(data))

