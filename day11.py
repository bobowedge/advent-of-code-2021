data = open("data/day11.txt").read().splitlines()
data = [[int(x) for x in list(y)] for y in data]

def flash(data, x, y, flash_set):
    flash_set.add((x,y))
    data[x][y] = 0
    for i in range(x-1, x+2):
        if 0 <= i < 10:
            for j in range(y-1, y+2):
                if 0 <= j < 10:
                    if (i,j) not in flash_set:
                        data[i][j] = data[i][j] + 1
                        if data[i][j] > 9:
                            flash(data, i, j, flash_set)

def solution1(data, turns):
    flashes = 0
    for i in range(turns):
        flash_set = set()
        for x in range(10):
            for y in range(10):
                if (x,y) not in flash_set:
                    data[x][y] = data[x][y] + 1
                    if data[x][y] > 9:
                        flash(data, x, y, flash_set)
        flashes += len(flash_set)
    return flashes

def solution2(data):
    turns = 100  # From solution 1
    while (True):
        flash_set = set()
        for x in range(10):
            for y in range(10):
                if (x,y) not in flash_set:
                    data[x][y] = data[x][y] + 1
                    if data[x][y] > 9:
                        flash(data, x, y, flash_set)
        turns += 1
        if(len(flash_set) == 100):
            return turns


print(f"Solution 1: {solution1(data, 100)}")
print(f"Solution 2: {solution2(data)}")

                