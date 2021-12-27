data = open("data/day20.txt").read().splitlines()

def convert(b):
    if b == "#":
        return 1
    else: 
        return 0

algo = [convert(x) for x in data[0]]
input_image = [[convert(x) for x in s] for s in data[2:]]

def lookup(image, i, j, default):
    s = ""
    for px,py in [(i-1,j-1), (i-1,j),  (i-1,j+1),
                  (  i,j-1), (  i,j),  (  i,j+1),
                  (i+1,j-1), (i+1,j),  (i+1,j+1)]:
        if 0 <= px < len(image) and 0 <= py < len(image[0]):
            s += str(image[px][py])
        else:
            s += default
    return int(s,2)

def enhance(image, default):
    rows = len(image) + 2
    cols = len(image[0]) + 2
    output_image = [[0 for i in range(cols)] for j in range(rows)]
    for x in range(rows):
        for y in range(cols):
            key = lookup(image, x-1, y-1, default)
            value = algo[key]
            output_image[x][y] = value
    return output_image

def solution1(im):
    im = enhance(im,"0")
    im = enhance(im,"1")
    return sum([sum(x) for x in im])

print("Solution 1:",solution1(input_image))

def solution2(im):
    for i in range(50):
        if i % 2 == 0:
            im = enhance(im,"0")
        else:
            im = enhance(im,"1")
    return sum([sum(x) for x in im])

print("Solution 1:",solution2(input_image))