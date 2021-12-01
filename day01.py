data = open("data/day01.txt").read().splitlines()
data = [int(line) for line in data]

counter1 = 0
previous_value = None
for value in data:
    if previous_value is not None and value > previous_value:
        counter1 += 1
    previous_value = value
print(f"Solution 1: {counter1}")

def window(iterable, k):
    for i in range(len(iterable)-k+1):
        yield iterable[i:i+k]

counter2 = 0
previous_value = None
for group in window(data, 3):
    value = sum(group)
    if previous_value is not None and value > previous_value:
        counter2 += 1
    previous_value = value
print(f"Solution 2: {counter2}")



