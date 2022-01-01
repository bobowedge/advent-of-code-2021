import re
data = open("data/day22.txt").read().splitlines()

pattern = re.compile("(on|off) x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)")

def solution1(data):
    cubes = set()
    for line in data:
        match = pattern.search(line)
        x1 = max(int(match.group(2)),-50)
        x2 = min(int(match.group(3))+1,51)
        y1 = max(int(match.group(4)),-50)
        y2 = min(int(match.group(5))+1,51)
        z1 = max(int(match.group(6)),-50)
        z2 = min(int(match.group(7))+1,51)
        for x in range(x1,x2):
            for y in range(y1,y2):
                for z in range(z1,z2):
                    if match.group(1) == "on":
                        cubes.add((x,y,z))
                    else:
                        cubes.discard((x,y,z))
    return len(cubes)

print("Solution 1:",solution1(data))

def overlap(cube1, cube2):
    if (cube2[0] > cube1[1] or cube2[1] < cube1[0] or
        cube2[2] > cube1[3] or cube2[3] < cube1[2] or
        cube2[4] > cube1[5] or cube2[5] < cube1[4]):
        return False
    return True

def combine(cube1, cube2):
    if not overlap(cube1, cube2):
        return [cube1, cube2]
    xs = [cube1[0],cube1[1],cube2[0],cube2[1]]
    ys = [cube1[2],cube1[3],cube2[2],cube2[3]]
    zs = [cube1[4],cube1[5],cube2[4],cube2[5]]
    xs.sort()
    ys.sort()
    zs.sort()
    cubes = []
    overlap_cube = (xs[1],xs[2],ys[1],ys[2],zs[1],zs[2])
    cubes.append(overlap_cube)
    
    if xs[0] == cube1[0]:
        cubex1 = (xs[0],xs[1]-1,cube1[2],cube1[3],cube1[4],cube1[5])
    else:
        cubex1 = (xs[0],xs[1]-1,cube2[2],cube2[3],cube2[4],cube2[5])

    if xs[3] == cube1[1]:
        cubex2 = (xs[2]+1,xs[3],cube1[2],cube1[3],cube1[4],cube1[5])
    else:
        cubex2 = (xs[2]+1,xs[3],cube2[2],cube2[3],cube2[4],cube2[5])

    if ys[0] == cube1[2]:
        cubey1 = (xs[1],xs[2],ys[0],ys[1]-1,cube1[4],cube1[5])
    else:
        cubey1 = (xs[1],xs[2],ys[0],ys[1]-1,cube2[4],cube2[5])

    if ys[3] == cube1[3]:
        cubey2 = (xs[1],xs[2],ys[2]+1,ys[3],cube1[4],cube1[5])
    else:
        cubey2 = (xs[1],xs[2],ys[2]+1,ys[3],cube2[4],cube2[5])

    cubez1 = (xs[1],xs[2],ys[1],ys[2],zs[0],zs[1]-1)
    cubez2 = (xs[1],xs[2],ys[1],ys[2],zs[2]+1,zs[3])

    for c in [cubex1,cubex2,cubey1,cubey2,cubez1,cubez2]:
        if c[0] <= c[1] and c[2] <= c[3] and c[4] <= c[5]:
            cubes.append(c)
    return cubes

def delete(cube1, cube2):
    if not overlap(cube1, cube2):
        return [cube1]

    xs = [cube1[0],cube1[1],cube2[0],cube2[1]]
    ys = [cube1[2],cube1[3],cube2[2],cube2[3]]
    zs = [cube1[4],cube1[5],cube2[4],cube2[5]]
    xs.sort()
    ys.sort()
    zs.sort()
    cubes = []

    cubex1 = None
    if xs[0] == cube1[0]:
        cubex1 = (xs[0],xs[1]-1,cube1[2],cube1[3],cube1[4],cube1[5])

    cubex2 = None
    if xs[3] == cube1[1]:
        cubex2 = (xs[2]+1,xs[3],cube1[2],cube1[3],cube1[4],cube1[5])

    cubey1 = None
    if ys[0] == cube1[2]:
        cubey1 = (xs[1],xs[2],ys[0],ys[1]-1,cube1[4],cube1[5])

    cubey2 = None
    if ys[3] == cube1[3]:
        cubey2 = (xs[1],xs[2],ys[2]+1,ys[3],cube1[4],cube1[5])

    cubez1 = None
    if zs[0] == cube1[4]:
        cubez1 = (xs[1],xs[2],ys[1],ys[2],zs[0],zs[1]-1)
    
    cubez2 = None
    if zs[3] == cube1[5]:
        cubez2 = (xs[1],xs[2],ys[1],ys[2],zs[2]+1,zs[3])

    for c in [cubex1,cubex2,cubey1,cubey2,cubez1,cubez2]:
        if (c is not None and
            c[0] <= c[1] and c[2] <= c[3] and c[4] <= c[5]):
            cubes.append(c)
    return cubes

def count_cube(cube):
    x = cube[1] - cube[0] + 1
    y = cube[3] - cube[2] + 1
    z = cube[5] - cube[4] + 1
    return x*y*z

def solution2(data):
    cubes = []
    index = 0
    for line in data:
        match = pattern.search(line)
        off = (match.group(1) == "off")
        x1 = int(match.group(2))
        x2 = int(match.group(3))
        y1 = int(match.group(4))
        y2 = int(match.group(5))
        z1 = int(match.group(6))
        z2 = int(match.group(7))
        new_cube = (x1,x2,y1,y2,z1,z2)
        new_cubes = []
        if off:
            for c in cubes:
                partition = delete(c, new_cube)
                new_cubes.extend(partition)
        else:
            overlaps = []
            for c in cubes:
                if not overlap(c, new_cube):
                    new_cubes.append(c)
                else:
                    overlaps.append(c)
            if len(overlaps) == 0:
                new_cubes.append(new_cube)
            elif len(overlaps) == 1:
                partition = combine(overlaps[0],new_cube)
                new_cubes.extend(partition)
            else:
                new_overlaps = []
                for co in overlaps:
                    partition = combine(co,new_cube)
                    new_overlaps.extend(partition)
                while(len(new_overlaps) > 0):
                    c1 = new_overlaps.pop(0)
                    c1overlap = False
                    j = None
                    for i,c2 in enumerate(new_overlaps):
                        if overlap(c1,c2):
                            c1overlap = True
                            j = i
                            break
                    if not c1overlap:
                        new_cubes.append(c1)
                        continue
                    c2 = new_overlaps.pop(j)
                    partition = combine(c1, c2)
                    new_overlaps.extend(partition)
        cubes = new_cubes
        index += 1
    
    total = 0
    for c in cubes:
        total += count_cube(c)
    return total
    
print("Solution 2:",solution2(data))


