
import re

#data = "target area: x=20..30, y=-10..-5"
data = "target area: x=207..263, y=-115..-63"

def advance(t):
    xpos, ypos, xvel, yvel = t
    new_xvel = 0
    if xvel > 0:
        new_xvel = xvel - 1
    elif xvel < 0:
        new_xvel = xvel + 1
    return xpos+xvel, ypos+yvel, new_xvel, yvel-1


def parse(data):
    match = re.search("target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)", data)
    xmin = int(match.group(1))    
    xmax = int(match.group(2))
    ymin = int(match.group(3))
    ymax = int(match.group(4))
    return xmin, xmax, ymin, ymax

def solution1(data):
    targetx1, targetx2, targety1, targety2 = parse(data)
    highesty=0
    for startxvel in range(1,targetx2):
        for startyvel in range(targety1,1000):
            t = (0, 0, startxvel, startyvel)
            target_hit = False
            highestytest = 0
            while t[0] <= targetx2 and t[1] >= targety1:
                t = advance(t)
                if targetx1 <= t[0] <= targetx2 and targety1 <= t[1] <= targety2:
                    target_hit = True
                    break
                if t[1] > highestytest:
                    highestytest = t[1]
            if target_hit:
                highesty = max(highesty, highestytest)
    return highesty

print(f"Solution 1: {solution1(data)}")

def solution2(data):
    targetx1, targetx2, targety1, targety2 = parse(data)
    unique = set()
    for startxvel in range(1,targetx2+1):
        for startyvel in range(targety1,1000):
            t = (0, 0, startxvel, startyvel)
            target_hit = False
            while t[0] <= targetx2 and t[1] >= targety1:
                t = advance(t)
                if targetx1 <= t[0] <= targetx2 and targety1 <= t[1] <= targety2:
                    target_hit = True
                    break
            if target_hit:
                unique.add((startxvel, startyvel))
    return len(unique)

print(f"Solution 2: {solution2(data)}")