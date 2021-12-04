
data = open("data/day03.txt").read().splitlines()
#data = open("data/test03.txt").read().splitlines()
size = len(data[0])

zeros = {}
ones = {}
for i in range(size):
    zeros[i] = 0
    ones[i] = 0

for line in data:
    for i in range(size):
        if line[i] == "0":
            zeros[i] += 1
        else:
            ones[i] += 1

gamma = ""
for i in range(size):
    if zeros[i] > ones[i]:
        gamma = gamma + "0"
    elif ones[i] > zeros[i]:
        gamma = gamma + "1"
    else:
        print(i, "BLAH")

gamma = int(gamma, 2)
epsilon = gamma ^ (2**size - 1)
print(f"Solution 1: {gamma*epsilon}")

def get_rating(data, flag):
    r = set(data)
    position = 0
    while(len(r) > 1):
        count0 = 0
        for n in r:
            if n[position] == "0":
                count0 += 1
        temp_set = set(r)
        for n in r:
            if flag:
                if count0 > len(r)/2:
                    if n[position] == "1":
                        temp_set.remove(n)
                elif n[position] == "0":
                    temp_set.remove(n)
            else:
                if count0 <= len(r)/2:
                    if n[position] == "1":
                        temp_set.remove(n)
                elif n[position] == "0":
                    temp_set.remove(n)
        r = set(temp_set)
        position += 1
    return int(r.pop(), 2)

oxygen = get_rating(data, True)
co2 = get_rating(data, False)
print(f"Solution 2: {oxygen*co2}")
   






