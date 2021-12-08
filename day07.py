import math

data = open("data/day07.txt").read().split(",")

data = [int(x) for x in data]

def solution1(data):
    dataset = set(data)
    best_fuel = None
    for x in dataset:
        fuel = sum([abs(y-x) for y in data])
        if best_fuel is None or fuel < best_fuel:
            best_fuel = fuel
    return best_fuel

print(f"Solution 1: {solution1(data)}")

def cost(n):
    return n*(n+1)//2

def solution2(data):
    dmin = min(data)
    dmax = max(data)
    best_fuel = None
    for i in range(dmin, dmax+1):
        fuel = [cost(abs(y-i)) for y in data]
        fuel = sum(fuel)
        if best_fuel is None or fuel < best_fuel:
            best_fuel = fuel
    return best_fuel

print(f"Solution 2: {solution2(data)}")