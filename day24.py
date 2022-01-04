import re 
import itertools

data = open("data/day24.txt").read().splitlines()

cmd = re.compile("(\S+) (\S+) (\S+)")

addx = []
addy = []
divz = []
for i in range(len(data)):
    if i % 18 == 4:
        match = cmd.match(data[i])
        if match.group(1) != "div" and match.group(2) != "z":
            print("ARGH4")
        divz.append(int(match.group(3)))
    elif i % 18 == 5:
        match = cmd.match(data[i])
        addx.append(int(match.group(3)))
        if match.group(1) != "add" and match.group(2) != "x":
            print("ARGH5")
    elif i % 18 == 15:
        match = cmd.match(data[i])
        addy.append(int(match.group(3)))
        if match.group(1) != "add" and match.group(2) != "y":
            print("ARGH15")

def f(z,w,i):
    x = (z % 26) + addx[i]
    z = int(z/divz[i])
    if x != w:
        z *= 26
        z += w + addy[i]
    return z

def invf(z, i):
    results = []
    if divz[i] == 1:
        # Option 1: x == w
        x = (z % 26) + addx[i]
        if 1 <= x <= 9:
            results.append((z,x))
        # Option 2: x != w
        w = z % 26
        w -= addy[i]
        if w < 0:
            w += 26
        if x != w and 1 <= w <= 9:
            oldz = (z - w - addy[i])//26
            results.append((oldz,w))
    else:
        # Option 1: x == w  
        for oldz in range(z*26,(z+1)*26):
            x = (oldz%26) + addx[i]
            if 1 <= x <= 9:
                results.append((oldz,x))
        # Option 2: x != w
        w = z % 26
        w -= addy[i]
        if w < 0:
            w += 26
        if 1 <= w <= 9:
            zstar = (z - w - addy[i])//26
            for oldz in range(zstar*divz[i],(zstar+1)*divz[i]):
                x = (oldz % 26) + addx[i]
                if x != w:
                    results.append((oldz,w))
    return set(results)

results = [(0,'')]
for i in range(13,-1,-1):
    new_results = []
    for zw in results:
        previous = invf(zw[0],i)
        oldw = zw[1]
        for (z,w) in previous:
            neww = str(w) + oldw
            if i > 0:
                new_results.append((z,neww))
            else:
                new_results.append(neww)
    results = new_results

results.sort()
print(results[-1], results[0])
