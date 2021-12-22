from math import prod

def bin_format(data):
    output = ""
    for i in range(len(data)):
        v = int(data[i],16)
        b = format(v, "04b")
        output += b
    return output

data = open("data/day16.txt").read()
data = bin_format(data)

def parse_literal(d):
    i = 0
    literal = ""
    while True:
        literal += d[i+1:i+5]
        i += 5
        if d[i-5] == "0":
            break
    return i, int(literal, 2)

def parse1(data, length, pkt_count=1000):
    index = 0
    total_version = 0
    count = 0
    while index < length and count < pkt_count:
        count += 1
        if data[index:] == "0"*(len(data)-index):
            break
        pversion = int(data[index:index+3], 2)
        ptypeId = int(data[index+3:index+6], 2)
        total_version += pversion
        index += 6
        if ptypeId == 4:
            psize, value = parse_literal(data[index:])
            index += psize
        else:
            if data[index] == "0":
                psize = int(data[index+1:index+16], 2)
                index += 1 + 15
                psize, pv = parse1(data[index:], psize, 1000)
                total_version += pv
                index += psize
            else:
                num_packets = int(data[index+1:index+12], 2)
                index += 1 + 11
                psize, pv = parse1(data[index:], len(data), num_packets)
                index += psize
                total_version += pv
    return index, total_version

print(parse1(data, len(data)))

def parse2(data, length, pkt_count, parent_type):
    index = 0
    count = 0
    values = []
    while index < length and count < pkt_count:
        count += 1
        if data[index:] == "0"*(len(data)-index):
            break
        pversion = int(data[index:index+3], 2)
        ptypeId = int(data[index+3:index+6], 2)
        index += 6
        if ptypeId == 4:
            psize, pvalue = parse_literal(data[index:])
            values.append(pvalue)
            index += psize
        else:
            if data[index] == "0":
                psize = int(data[index+1:index+16], 2)
                index += 16
                psize, pvalue = parse2(data[index:], psize, 1000, ptypeId)
                values.append(pvalue)
                index += psize
            else:
                num_packets = int(data[index+1:index+12], 2)
                index += 12
                psize, pvalue = parse2(data[index:], len(data), num_packets, ptypeId)
                values.append(pvalue)
                index += psize
    if parent_type == 0:
        value = sum(values)
    elif parent_type == 1:
        value = prod(values)
    elif parent_type == 2:
        value = min(values)
    elif parent_type == 3:
        value = max(values)
    elif parent_type == 5:
        if values[0] > values[1]:
            value = 1
        else:
            value = 0
    elif parent_type == 6:
        if values[0] < values[1]:
            value = 1
        else:
            value = 0
    elif parent_type == 7:
        if values[0] == values[1]:
            value = 1
        else:
            value = 0
    return index, value

print(parse2(data, len(data), 1000, 0))