import numpy as np


def parse(data):
    calls = [int(x) for x in data[0].split(",")]
    boards = []
    index = 2
    while index < len(data):
        lines = data[index:index+5]
        lines = [x.split() for x in lines]
        lines = [[int(y) for y in x] for x in lines]
        lines = np.array(lines)
        index += 6
        boards.append(lines)
    return calls, boards


def check_bingo(mask):
    row_check = (~mask.any(axis=1)).any()
    col_check = (~mask.any(axis=0)).any()
    return row_check or col_check


data = open("data/day04.txt").read().splitlines()
calls, boards = parse(data)


def solution1(calls, boards):
    masks = np.ones((len(boards), 5, 5), dtype=np.int8)
    value = 0
    for i, call in enumerate(calls):
        for j, board in enumerate(boards):
            result = np.where(board == call, 0, 1)
            masks[j] &= result
            bingo = check_bingo(masks[j])
            if bingo:
                result = np.where(masks[j] == 0, 0, board)
                value = np.sum(result)
                break
        if bingo:
            value *= call
            return value
    raise RuntimeError("No valid board")


value1 = solution1(calls, boards)
print(f"Solution1: {value1}")


def solution2(calls, boards):
    masks = np.ones((len(boards), 5, 5), dtype=np.int8)
    last_call = None
    last_board = None
    for j, board in enumerate(boards):
        for i, call in enumerate(calls):
            result = np.where(board == call, 0, 1)
            masks[j] &= result
            bingo = check_bingo(masks[j])
            if bingo:
                if last_call is None or last_call < i:
                    last_call = i
                    last_board = j
                break
    board = boards[last_board]
    result = np.where(masks[last_board] == 0, 0, board)
    value = np.sum(result)
    value *= calls[last_call]
    return value


value2 = solution2(calls, boards)
print(f"Solution2: {value2}")