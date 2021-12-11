data = open("data/day10.txt").read().splitlines()

score1Dict = {')':3,']':57,'}':1197,'>':25137}
score2Dict = {'(':1,'[':2,'{':3,'<':4}
def solutions(data):
    score1 = 0
    scores2 =[]
    for line in data:
        corrupted = None
        parse = []
        for x in line:
            if ( (x == ')' and parse[-1] != '(') or
                 (x == ']' and parse[-1] != '[') or
                 (x == '}' and parse[-1] != '{') or
                 (x == '>' and parse[-1] != '<') ):
                corrupted = x
                break
            elif x in [')',']','}','>']:
                if len(parse) > 0:
                    parse.pop(-1)
                else:
                    corrupted = x
                    break
            else:
                parse.append(x)
        if corrupted is not None:
            score1 += score1Dict[corrupted]
        else:
            score2 = 0
            parse.reverse()
            for x in parse:
                score2 *= 5
                score2 += score2Dict[x]
            scores2.append(score2)
    scores2.sort()
    slen = len(scores2)
    middle = (slen - 1) // 2
    return score1, scores2[middle]

s = solutions(data)
print(f"Solution 1: {s[0]}")
print(f"Solution 2: {s[1]}")

                
