data = open("data/day06.txt").read().splitlines()

lanternfish = data[0].split(",")
lanternfish = [int(x) for x in lanternfish]

def solution(lanternfish, days):
    lanterndict = {}
    total = 0
    for x in lanternfish:
        lanterndict[x] = lanterndict.get(x, 0) + 1
        total += 1

    for day in range(days):
        new_dict = {}        
        for d in lanterndict:
            n = lanterndict[d]
            if d > 0:
                new_dict[d-1] = new_dict.get(d-1,0) + n
            else:
                new_dict[6] = new_dict.get(6,0) + n
                new_dict[8] = n
                total += n
        lanterndict = new_dict
    return total

print(f"Solution 1: {solution(lanternfish,80)}")
print(f"Solution 1: {solution(lanternfish,256)}")

