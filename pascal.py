#!/usr/bin/python3

def next(lst, result = []):
    return next(lst[1:], [lst[0] + lst[1]] + result) if len(lst) > 1 else result

# searchs element x, y of Pascal triangle with tail recutsion
def pascal(x, y, lst = [1], r = 0):
    return pascal(x, y, [1] + next(lst) + [1], r + 1) if r < y else lst[x]

