# Test data
#start1, start2 = 4, 8  
# Input data
start1, start2 = 10, 9

def solution1(start1, start2):
    die = range(100)
    points1, points2 = 0, 0
    pos1, pos2 = start1, start2

    i = 1
    turn = 0
    while max(points1, points2) < 1000:
        rolls = 0
        for j in range(3):
            rolls += i
            i += 1
            if i == 101:
                i = 1
        if turn % 2 == 0:
            pos1 += rolls
            if pos1 > 10:
                pos1 %= 10
                if pos1 == 0:
                    pos1 += 10
            points1 += pos1
        else:
            pos2 += rolls 
            if pos2 > 10:
                pos2 %= 10
                if pos2 == 0:
                    pos2 += 10
            points2 += pos2
        turn += 1
    return 3 * turn * min(points1, points2)

print("Solution 1:", solution1(start1,start2))

def solution2(start1, start2):
    turn_universe = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}
    universes = {(start1,start2,0,0):1}
    wins1 = 0
    wins2 = 0
    turn = 0
    while(len(universes) > 0):
        new_universes = {}
        for key in universes:
            pos1, pos2, score1, score2 = key
            old_unis = universes[key]
            for t in turn_universe:
                new_unis = turn_universe[t] * old_unis
                if turn % 2 == 0:
                    new_pos = pos1 + t
                else:
                    new_pos = pos2 + t
                if new_pos > 10:
                    new_pos %= 10
                    if new_pos == 0:
                        new_pos = 10
                if turn % 2 == 0:
                    new_score = score1 + new_pos
                    if new_score >= 21:
                        wins1 += new_unis
                    else:
                        new_key = (new_pos,pos2,new_score,score2)
                        new_universes[new_key] = new_universes.get(new_key, 0) + new_unis
                else:
                    new_score = score2 + new_pos
                    if new_score >= 21:
                        wins2 += new_unis
                    else:
                        new_key = (pos1,new_pos,score1,new_score)
                        new_universes[new_key] = new_universes.get(new_key, 0) + new_unis   
        universes = new_universes      
        print(turn, wins1, wins2)
        turn += 1
        if turn > 25:
            print("Turn break")
            break
    return max(wins1, wins2)
                    

print("Solution 2:", solution2(start1,start2))