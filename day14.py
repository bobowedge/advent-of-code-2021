data = open("data/day14.txt").read().splitlines()

start = data[0]
map = {}
for line in data[2:]:
    line = line.split()
    map[line[0]] = line[2]

def get_chain(start, map, steps):
    chain = list(start)
    for i in range(steps):
        new_chain = []
        for j in range(len(chain)-1):
            pair = "".join(chain[j:j+2])
            insert = map[pair]
            new_chain.append(chain[j])
            new_chain.append(insert)
        new_chain.append(chain[-1])
        chain = new_chain
    return chain

def solution1(start, map, steps=10):
    chain = get_chain(start, map, steps)
    values = set(chain)
    minc = len(chain)
    maxc = 0
    for v in values:
        c = chain.count(v)
        if c < minc:
            minc = c
        if c > maxc:
            maxc = c
    return maxc - minc

print(f"Solution 1: {solution1(start,map)}")

def get_pairs(start, map):
    values = set(list(start))
    for x in map.values():
        values.add(x)
    pairs = set()
    for x in values:
        for y in values:
            pairs.add(x+y)
    return pairs

def count_pairs(chain):
    chain_map = {}
    for i in range(len(chain) - 1):
        pair = chain[i:i+2]
        chain_map[pair] = chain_map.get(pair,0) + 1
    return chain_map

def get_counts_diff(start, pair_map):
    counts = {}
    for i in range(len(start) - 1):
        pair = start[i:i+2]
        pmp = pair_map[pair]
        for p in pmp:
            counts[p[0]] = counts.get(p[0],0) + pmp[p]
            counts[p[1]] = counts.get(p[1],0) + pmp[p]
    minc = None
    maxc = None
    for c in counts:
        value = counts[c]
        if c in [start[0],start[-1]]:
            value += 1
        value //= 2
        if minc is None or value < minc:
            minc = value
        if maxc is None or value > maxc:
            maxc = value
    return maxc - minc

def get_pair_map10(start, map):
    pairs = get_pairs(start, map)
    pair_map = {}
    for p in pairs:
        chainp = "".join(get_chain(p, map, 10))
        chainp_map = count_pairs(chainp)
        pair_map[p] = chainp_map
    return pair_map
    
def get_pair_map20(start, map):
    pairs = get_pairs(start, map)
    pair_map10 = get_pair_map10(start, map)
    pair_map20 = {}
    for p1 in pair_map10:
        p1map = pair_map10[p1]
        pmap20 = {}
        for p2 in p1map:
            p2map = pair_map10[p2]
            for p3 in p2map:
                pmap20[p3] = pmap20.get(p3, 0) + p2map[p3] * p1map[p2]
        pair_map20[p1] = pmap20
    return pair_map20

def get_pair_map40(start, map):
    pairs = get_pairs(start, map)
    pair_map20 = get_pair_map20(start, map)
    pair_map40 = {}
    for p1 in pair_map20:
        p1map = pair_map20[p1]
        pmap40 = {}
        for p2 in p1map:
            p2map = pair_map20[p2]
            for p3 in p2map:
                pmap40[p3] = pmap40.get(p3, 0) + p2map[p3] * p1map[p2]
        pair_map40[p1] = pmap40
    return pair_map40

def solution2(start,map):
    pmp40 = get_pair_map40(start, map)
    diff = get_counts_diff(start, pmp40)
    return diff

print(f"Solution 2: {solution2(start,map)}")
