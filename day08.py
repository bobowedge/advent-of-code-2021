data = open("data/day08.txt").read().splitlines()

def solution1(data):
    counts = 0
    for line in data:
        x, y = line.split("|")
        y = y.split()
        for z in y:
            if len(z) in [2, 3, 4, 7]:
                counts += 1
    return counts

print(f"Solution 1: {solution1(data)}")

def solution2(data):
    total = 0
    for line in data:
        x, y = line.split("|")
        x = [frozenset(z) for z in x.split()]
        xmap = {}
        mmap = [None for i in range(10)]
        for seg in x:
            if len(seg) == 2:
                xmap[seg] = 1
                mmap[1] = seg
            elif len(seg) == 3:
                xmap[seg] = 7
                mmap[7] = seg
            elif len(seg) == 4:
                xmap[seg] = 4
                mmap[4] = seg
            elif len(seg) == 7:
                xmap[seg] = 8
                mmap[8] = seg
        cand5 = []
        cand0 = []
        for seg in x:
            blah = mmap[1].intersection(seg)
            if len(seg) == 5:
                if len(blah) == 2:
                    xmap[seg] = 3
                    mmap[3] = seg
                else:
                    cand5.append(seg)
            if len(seg) == 6: 
                if len(blah) != 2:
                    xmap[seg] = 6
                    mmap[6] = seg
                else:
                    cand0.append(seg)
        c51 = cand5[0].intersection(cand0[0])
        c52 = cand5[0].intersection(cand0[1])
        if len(c51) == 5 or len(c52) == 5:
            xmap[cand5[0]] = 5
            xmap[cand5[1]] = 2
            mmap[5] = cand5[0]
            mmap[2] = cand5[1]
        else:
            xmap[cand5[0]] = 2
            xmap[cand5[1]] = 5
            mmap[2] = cand5[0]
            mmap[5] = cand5[1]
        c91 = mmap[3].intersection(cand0[0])
        if len(c91) == 5:
            xmap[cand0[0]] = 9
            xmap[cand0[1]] = 0
            mmap[9] = cand0[0]
            mmap[0] = cand0[1]
        else:
            xmap[cand0[0]] = 0
            xmap[cand0[1]] = 9
            mmap[0] = cand0[0]
            mmap[9] = cand0[1]
        y = [str(xmap[frozenset(z)]) for z in y.split()]
        y = "".join(y)
        y = int(y)
        total += y
    return total

print(f"Solution 2: {solution2(data)}")
