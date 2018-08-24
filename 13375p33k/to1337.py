#!/usr/bin/python3

import sys

alpha = {
	'A': '4',
	'B': '8',
	'C': '(',
	'D': ')',
	'E': '3',
	'F': '#',
	'G': '9',
	'H': 'l-l',
	'L': '1',
	'J': '_l',
	'K': 'l<',
	'P': 'l>',
	'Q': '&',
	'R': 'l2',
	'S': '5',
	'T': '7',
	'U': 'l_l',
	'V': '\/',
	'W': '\/\/',
	'X': '><',
	'Y': 'Y',
	'Z': '2'
}

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

buffer = []
for c in f.read().upper():
    buffer.append(alpha[c] if c in alpha else c)

print(''.join(buffer))
