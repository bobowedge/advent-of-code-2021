data = open("data/day05.txt").read().splitlines()

def solution1(data):
    points = {}
    for line in data:
        line = line.split()
        x1, y1 = line[0].split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2, y2 = line[-1].split(",")
        x2 = int(x2)
        y2 = int(y2)
        if x1 == x2:
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            for y in range(ymin, ymax + 1):
                points[(x1,y)] = points.get((x1,y), 0) + 1
        elif y1 == y2:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            for x in range(xmin, xmax + 1):
                points[(x,y1)] = points.get((x,y1), 0) + 1
    result = 0
    for value in points.values():
        if value > 1:
            result += 1
    return result

soln1 = solution1(data)
print(f"Solution 1: {soln1}")

def solution2(data):
    points = {}
    for line in data:
        line = line.split()
        x1, y1 = line[0].split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2, y2 = line[-1].split(",")
        x2 = int(x2)
        y2 = int(y2)
        slopex = x2 - x1
        slopey = y2 - y1
        x, y = x1, y1
        points[(x,y)] = points.get((x,y), 0) + 1
        while((x,y) != (x2, y2)):
            if slopex < 0:
                x -= 1
            elif slopex > 0:
                x += 1
            if slopey < 0:
                y -= 1
            elif slopey > 0:
                y += 1
            points[(x,y)] = points.get((x,y), 0) + 1
    result = 0
    for value in points.values():
        if value > 1:
            result += 1
    return result

soln2 = solution2(data)
print(f"Solution 2: {soln2}")