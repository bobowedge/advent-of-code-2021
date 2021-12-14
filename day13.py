data = open("data/day13.txt").read().splitlines()

points = set()
folds = []
for line in data:
    line = line.strip()
    if len(line) == 0:
        continue
    if "fold" in line:
        line = line.split()
        axis,value = line[-1].split("=")
        folds.append((axis,int(value)))
    else:
        x,y = line.split(",")
        points.add((int(x),int(y)))

def solution1(points, folds):
    new_points = set()

    for x,y in points:
        if folds[0][0] == 'x':
            if x > folds[0][1]:
                diff = x - folds[0][1]
                x = x - 2 * diff
        elif y > folds[0][1]:
            diff = y - folds[0][1]
            y = y - 2 * diff
        new_points.add((x,y))
    return len(new_points)

print(f"Solution 1: {solution1(points,folds)}")

def solution2(points, folds):
    
    for axis,value in folds:
        new_points = set()
        for x,y in points:
            if axis == 'x':
                if x > value:
                    diff = x - value
                    x = x - 2 * diff
            elif y > value:
                diff = y - value
                y = y - 2 * diff
            new_points.add((x,y))
        points = new_points
    
    for y in range(6):
        for x in range(40):
            if (x,y) in points:
                print("#",end='')
            else:
                print(".",end="")
        print("")

print("Solution 2:")
solution2(points,folds)