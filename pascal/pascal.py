#!/usr/bin/python3

import sys

# function pas
# searchs element x, y of Pascal triangle with tail recutsion
# params: x, y - element coords
#         l - list, current pascal triangle row
def pas(x, y, l = [1], r = 1):
    # lambda nxt
    # returns inner part of next row in pascal triangle
    # params: l - list, current pascal triangle 
    #         r - result
    # also uses tail recursion
    nxt = lambda l, r = []: nxt(l[1:], [l[0] + l[1]] + r) if len(l) > 1 else r

    # lambda one
    # gives empty list or list containing one element 1
    # according to passed bool value
    one = lambda x: [] if x else [1]

    return pas(x, y, one(r>y-x) + nxt(l) + one(r>x), r + 1) if r <= y else l[0]

if __name__ == '__main__':
    print(pas(int(sys.argv[1]), int(sys.argv[2])))
