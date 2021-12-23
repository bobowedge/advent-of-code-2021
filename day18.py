import re

#data = open("data/test18.txt").read().splitlines()

pattern1 = re.compile("\[(\d+)\,(\d+)\]")
pattern2 = re.compile("\d+")

def addition(x,y):
    return f"[{x},{y}]"

def explode(x:str):
    match = pattern1.search(x)
    while(match):
        first = match.start()
        last = match.end()
        left = x[:first].count("[")
        right = x[:first].count("]")
        diff = left - right
        if diff < 4:
            match = pattern1.search(x, last)
            continue
        n1 = int(match.group(1))
        n2 = int(match.group(2))
        newx = x[:first]
        for match_left in pattern2.finditer(x, 0, first):
            newn1 = n1 + int(match_left.group())
            mli1 = match_left.start()
            mli2 = match_left.end()
            newx = x[:mli1] + str(newn1) + x[mli2:first]
        newx += "0"
        match_right = pattern2.search(x, last)
        if match_right:
            n2 = n2 + int(match_right.group())
            mri1 = match_right.start()
            mri2 = match_right.end()
            newx += x[last:mri1] + str(n2) + x[mri2:]
        else:
            newx += x[last:]
        return newx
    return x

def split(x:str):
    for match in pattern2.finditer(x):
        n = int(match.group())
        if n <= 9:
            continue
        left = n // 2
        right = n - left
        return x[:match.start()] + f"[{left},{right}]" + x[match.end():]
    return x

def reduce(x:str):
    while(True):
        y = explode(x)
        if x == y:
            y = split(x)
            if x == y:
                return x
            x = y 
        x = y

def magnitude(x:str):
    match = pattern1.search(x)
    while(match):
        left = int(match.group(1))
        right = int(match.group(2))
        mag = 3*left + 2*right
        x = x[:match.start()] + str(mag) + x[match.end():]
        match = pattern1.search(x)
    return x

data = open("data/day18.txt").read().splitlines()

def solution1(data):
    x = data[0]
    for y in data[1:]:
        x = addition(x, y)
        x = reduce(x)
    return magnitude(x)

print(solution1(data))

def solution2(data):
    bestmag = 0
    for x in data:
        for y in data:
            z = addition(x,y)
            z = reduce(z)
            z = int(magnitude(z))
            if bestmag < z:
                bestmag = z
    return bestmag

print(solution2(data))