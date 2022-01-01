from heapq import heappush, heappop

state = [(2,1,'B'),(4,1,'C'),(6,1,'B'),(8,1,'D'),
         (2,2,'A'),(4,2,'D'),(6,2,'C'),(8,2,'A')]    
state = [(2,1,'A'),(4,1,'D'),(6,1,'B'),(8,1,'D'),
        (2,2,'B'),(4,2,'C'),(6,2,'A'),(8,2,'C')]  

hallway = set([(0,0),(1,0),(3,0),(5,0),(7,0),(9,0),(10,0)])

energy = {'A':1,'B':10,'C':100,'D':1000}

bins = {'A':2,'B':4,'C':6,'D':8}

def clear_path1(state, x1, y1, x2, y2):
    s = [(x,y) for (x,y,_) in state]
    if y1 == 0:
        if (x2,y2) in s:
            return False
        if y2 == 2 and (x2,1) in s:
            return False
        if x2 > x1:
            for i in range(x1+1,x2+1):
                if (i,0) in s:
                    return False
        else:
            for i in range(x1-1,x2-1,-1):
                if (i,0) in s:
                    return False
    else:
        if y1 == 2 and (x1,1) in s:
            return False
        if x2 > x1:
            for i in range(x1,x2+1):
                if (i,0) in s:
                    return False
        else:
            for i in range(x1,x2-1,-1):
                if (i,0) in s:
                    return False
    return True

def find_neighbors1(state:tuple):
    neighbors = {}
    for (x,y,z) in state:
        if y == 0:
            dest1 = (bins[z],1)
            dest2 = (bins[z],2)
            if (bins[z], 2, z) in state:
                dest = dest1
            else:
                dest = dest2
            clear = clear_path1(state, x, y, dest[0], dest[1])
            if clear:
                scopy = list(state)
                scopy.remove((x,y,z))
                scopy.append((dest[0],dest[1],z))
                scopy.sort()
                scopy = tuple(scopy)
                cost = (abs(x-dest[0]) + abs(y-dest[1]))*energy[z]
                neighbors[scopy] = cost
        else:
            for h1,h2 in hallway:
                clear = clear_path1(state, x, y, h1, h2)
                if clear:
                    scopy = list(state)
                    scopy.remove((x,y,z))
                    scopy.append((h1,h2,z))
                    scopy.sort()
                    scopy = tuple(scopy)
                    cost = (abs(x-h1) + abs(y-h2))*energy[z]
                    neighbors[scopy] = cost
    return neighbors

def heuristic(state):
    cost = 0
    s = {(x,y):z for (x,y,z) in state}
    for (x,y,z) in state:
        if y == 0:
            dx = bins[z]
            dy = 1
            cost += (abs(x-dx) + abs(y-dy))*energy[z]
        elif x == bins[z]:
            if y == 1:
                below = s.get((x,2),'F')
                if below != z:
                    cost += 4 * energy[z]
        else:
            cost += (abs(x-bins[z]) + y)*energy[z]
    return cost

def view(path,bottom=2):
    p = {(x,y):z for (x,y,z) in path}
    print("------------------------")
    print("#"*13)
    print('#',end='')
    for h in range(11):
        print(p.get((h,0),'.'),end='')
    print('#')

    for j in range(1,bottom+1):
        if j == 1:
            print('###',end='')
        else:
            print("  #",end="")
        for i in range(2,10,2):
            print(p.get((i,j),'.'),end='')
            print('#',end='')
        if j == 1:
            print('##',end="")
        print()
    print('  #########  ')
    print("------------------------")

def path_cost(state1, state2):
    s1 = {(x,y):z for (x,y,z) in state1}
    s2 = {(x,y):z for (x,y,z) in state2}
    k1 = set(s1.keys())
    k2 = set(s2.keys())
    diff = k1.symmetric_difference(k2)
    if len(diff) != 2:
        raise RuntimeError("BLAH")
    d1 = diff.pop()
    d2 = diff.pop()
    if d1 in s1:
        return energy[s1[d1]] * (abs(d1[0]-d2[0]) + abs(d1[1]-d2[1]))
    else:
        return energy[s2[d1]] * (abs(d1[0]-d2[0]) + abs(d1[1]-d2[1]))

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path

def A_star(start, final, h, find_neighbors):
    open_set = set()
    open_set.add(start)
    open_set_pq = [(h(start),start)]

    came_from = {}

    gscore = {}
    gscore[start] = 0

    fscore = {}
    fscore[start] = h(start)

    while len(open_set) > 0:
        score, current = heappop(open_set_pq)
        if current == final:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        neighbors = find_neighbors(current)
        for neighbor, cost in neighbors.items():
            tent_gscore = gscore[current] + cost
            if tent_gscore < gscore.get(neighbor,100000):
                came_from[neighbor] = current
                gscore[neighbor] = tent_gscore
                fscore[neighbor] = tent_gscore + h(neighbor)
                if neighbor not in open_set:
                    heappush(open_set_pq, (fscore[neighbor], neighbor))
                    open_set.add(neighbor)
    return None

def solution1(state):
    state.sort()
    start = tuple(state)

    final = []
    for i in range(1,3):
        final.append((2,i,'A'))
        final.append((4,i,'B'))
        final.append((6,i,'C'))
        final.append((8,i,'D'))
    
    final.sort()

    final = tuple(final)
    path = A_star(start, final, heuristic, find_neighbors1)
    cost = 0
    for i in range(len(path)-1,0,-1):
        # view(path[i])
        costp = path_cost(path[i],path[i-1])
        # print(costp)
        cost += costp
    # view(path[0])
    return cost 

print(solution1(state))

def clear_path2(state, x1, y1, x2, y2):
    s = set([(x,y) for (x,y,_) in state])
    if x2 > x1:
        for x in range(x1+1,x2+1):
            if (x,0) in s:
                return False
    else:
        for x in range(x1-1,x2-1,-1):
            if (x,0) in s:
                return False
    if y1 == 0:
        for y in range(1,y2+1):
            if (x2,y) in s:
                return False
    else:
        for y in range(y1-1,0,-1):
            if (x1,y) in s:
                return False
    return True

def find_neighbors2(state:tuple):
    neighbors = {}
    for (x,y,z) in state:
        if y == 0:
            dest = None
            lowest = 4
            while(dest is None):
                if (bins[z], lowest, z) in state:
                    lowest -= 1
                    continue
                dest = (bins[z],lowest)
            if dest is not None and clear_path2(state, x, y, dest[0], dest[1]):
                scopy = list(state)
                scopy.remove((x,y,z))
                scopy.append((dest[0],dest[1],z))
                scopy.sort()
                scopy = tuple(scopy)
                cost = (abs(x-dest[0]) + abs(y-dest[1]))*energy[z]
                neighbors[scopy] = cost
        else:
            for h1,h2 in hallway:
                if clear_path2(state, x, y, h1, h2):
                    scopy = list(state)
                    scopy.remove((x,y,z))
                    scopy.append((h1,h2,z))
                    scopy.sort()
                    scopy = tuple(scopy)
                    cost = (abs(x-h1) + abs(y-h2))*energy[z]
                    neighbors[scopy] = cost
    return neighbors

def solution2(state):
    new_state = []
    for (x,y,z) in state:
        if y == 2:
            new_state.append((x,4,z))
        else:
            new_state.append((x,y,z))
    new_state.extend([(2,2,'D'),(4,2,'C'),(6,2,'B'),(8,2,'A'),
                      (2,3,'D'),(4,3,'B'),(6,3,'A'),(8,3,'C')])
    new_state.sort()
    start = tuple(new_state)

    final = []
    for i in range(1,5):
        final.append((2,i,'A'))
        final.append((4,i,'B'))
        final.append((6,i,'C'))
        final.append((8,i,'D'))
    
    final.sort()
    final = tuple(final)

    path = A_star(start, final, heuristic, find_neighbors2)
    cost = 0
    for i in range(len(path)-1,0,-1):
        # view(path[i])
        costp = path_cost(path[i],path[i-1])
        # print(costp)
        cost += costp
    # view(path[0])
    return cost 

print(solution2(state))