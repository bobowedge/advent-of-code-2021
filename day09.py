data = open("data/day09.txt").read().splitlines()

def parse(data):
    output = []
    for line in data:
        line = list(line)
        line = [int(x) for x in line]
        output.append(line)
    return output

data = parse(data)

def solution1(data):
    risk_level = 0
    for i,row in enumerate(data):
        for j,col in enumerate(row):
            if i > 0:
                up = data[i-1][j]
            else:
                up = 10
            if i + 1 < len(data):
                down = data[i+1][j]
            else:
                down = 10
            if j > 0:
                left = data[i][j-1]
            else:
                left = 10
            if j + 1 < len(row):
                right = data[i][j+1]
            else:
                right = 10
            lowest = min(up, down, left, right)
            if col < lowest:
                risk_level += col + 1
    return risk_level

print(f"Solution 1: {solution1(data)}")

def add_to_basin(basin_points, i, j, data):
    basin_points.add((i,j))
    if i > 0:
        up = data[i-1][j]
        if up < 9 and (i-1,j) not in basin_points:
            add_to_basin(basin_points, i-1, j, data)
    if i + 1 < len(data):
        down = data[i+1][j]
        if down < 9 and (i+1,j) not in basin_points:
            add_to_basin(basin_points, i+1, j, data)
    if j > 0:
        left = data[i][j-1]
        if left < 9 and (i,j-1) not in basin_points:
            add_to_basin(basin_points, i, j-1, data)
    if j + 1 < len(data[0]):
        right = data[i][j+1]
        if right < 9 and (i,j+1) not in basin_points:
            add_to_basin(basin_points, i, j+1, data)

def solution2(data):
    low_points = set()
    for i,row in enumerate(data):
        for j,col in enumerate(row):
            if i > 0:
                up = data[i-1][j]
            else:
                up = 10
            if i + 1 < len(data):
                down = data[i+1][j]
            else:
                down = 10
            if j > 0:
                left = data[i][j-1]
            else:
                left = 10
            if j + 1 < len(row):
                right = data[i][j+1]
            else:
                right = 10
            lowest = min(up, down, left, right)
            if col < lowest:
                low_points.add((i,j))

    basin_sizes = []
    for x,y in low_points:
        basin_points = set()
        add_to_basin(basin_points, x, y, data)
        basin_sizes.append(len(basin_points))
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

print(f"Solution 2: {solution2(data)}")