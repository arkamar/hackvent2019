#! /bin/env python

import sys

tbl = {
    '00000': 'A',
    '00001': 'B',
    '00010': 'C',
    '00011': 'D',
    '00100': 'E',
    '00101': 'F',
    '00110': 'G',
    '00111': 'H',
    '01000': 'I',
    '01001': 'J',
    '01010': 'K',
    '01011': 'L',
    '01100': 'M',
    '01101': 'N',
    '01110': 'O',
    '01111': 'P',
    '10000': 'Q',
    '10001': 'R',
    '10010': 'S',
    '10011': 'T',
    '10100': 'U',
    '10101': 'V',
    '10110': 'W',
    '10111': 'X',
    '11000': 'Y',
    '11001': 'Z'
}

m = sys.stdin.read()

l = 5
o = ''
try:
    for i in range(0,len(m),l):
        o += tbl[m[i:i+l]]
except:
    pass

print(o)

