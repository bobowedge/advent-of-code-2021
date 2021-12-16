data = open("data/day15.txt").read().splitlines()
data = [[int(x) for x in list(y)] for y in data]

nodes = set()
distances = {}
ld = len(data)
for x in range(5*ld):
    for y in range(5*ld):
        nodes.add((x,y))
        m = {}
        if y > 0:
            val = data[x%ld][(y-1)%ld]
            val += x//ld + (y-1)//ld
            val = (val-1)%9 + 1
            m[(x,y-1)] = val
        if y + 1 < 5*ld:
            val = data[x%ld][(y+1)%ld]
            val += x//ld + (y+1)//ld
            val = (val-1)%9 + 1
            m[(x,y+1)] = val
        if x > 0:
            val = data[(x-1)%ld][y%ld]
            val += (x-1)//ld + y//ld
            val = (val-1)%9 + 1
            m[(x-1,y)] = val
        if x + 1 < 5*ld:
            val = data[(x+1)%ld][y%ld]
            val += (x+1)//ld + y//ld
            val = (val-1)%9 + 1
            m[(x+1,y)] = val
        distances[(x,y)] = m

def solutions(nodes, distances):
    unvisited = {node: None for node in nodes}
    visited = {}
    current = (0,0)
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    return visited[(ld-1,ld-1)], visited[(5*ld-1,5*ld-1)]

print(f"Solutions: {solutions(nodes,distances)}")

