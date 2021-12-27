import re

data = open("data/day19.txt").read().splitlines()

scanners = {}
for line in data:
    if len(line) == 0:
        continue
    match = re.search("--- scanner (\d+) ---", line)
    if match:
        scanner = int(match.group(1))
        continue
    match = re.search("(-?\d+),(-?\d+),(-?\d+)", line)
    x = int(match.group(1))
    y = int(match.group(2))
    z = int(match.group(3))
    l = scanners.get(scanner,[])
    l.append((x,y,z))
    scanners[scanner] = l

def roll(v):
    return (v[0],v[2],-v[1])

def turn(v):
    return (-v[1],v[0],v[2])

def rotate(s):
    for cycle in range(2):
        for step in range(3):
            s = [roll(v) for v in s]
            yield s
            for k in range(3):
                s = [turn(v) for v in s]
                yield s
        s = [roll(turn(roll(v))) for v in s]

def overlap(beacons1, s2):
    for (x1, y1, z1) in beacons1:
        for b2 in range(len(s2)):
            for rots2 in rotate(s2):
                t1, t2, t3 = rots2[b2]
                rots2 = set([(x1 - t1 + x, y1 - t2 + y, z1 - t3 + z) for (x,y,z) in rots2])
                if len(beacons1.intersection(rots2)) >= 12:
                    return x1-t1, y1-t2, z1-t3, rots2
    return None

def manhattan_dist(x,y):
    return abs(x[0]-y[0]) + abs(x[1] - y[1]) + abs(x[2]-y[2])

def solutions(scanners:dict):
    all_beacons = set(scanners[0])
    unfound_scanners = list(scanners.keys())
    unfound_scanners.remove(0)
    scanner_locations = set()
    scanner_locations.add((0,0,0))
    while(len(unfound_scanners) > 0):
        scanner = unfound_scanners.pop(0)
        new_beacons = overlap(all_beacons, scanners[scanner])
        if new_beacons is not None:
            sx, sy, sz, new_beacons = new_beacons
            all_beacons = all_beacons.union(new_beacons)
            scanner_locations.add((sx,sy,sz))
        else:
            unfound_scanners.append(scanner)
    soln1 = len(all_beacons)
    biggest_diff = 0
    for x in scanner_locations:
        for y in scanner_locations:
            d = manhattan_dist(x,y)
            if d > biggest_diff:
                biggest_diff = d
    return soln1, biggest_diff

print("Solutions:", solutions(scanners))


