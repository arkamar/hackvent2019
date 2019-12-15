#! /bin/env python

from base64 import b64decode

m = '52982 16149 42355 19148 64755 13012 9447 7791 30804 32219 29904 19309 27474 48765 4140 58322 58509 41037 30575 22237 56513 28118 54008 14908 17998 49290 61171 40740 29705 32258 8745 19415 23698 6173 1383 31743 13716 41602 58542 27945 59984 61085 29346 64361 25437'
n = [int(i) for i in m.split()]

initvector = 0x1337c0de

def nextnumber():
    global initvector
    initvector = (initvector * 16807) & 0xffffffff
    return initvector

counter = 0
def get2bytes():
    global counter
    o = n[counter] ^ (nextnumber() & 0xdead)
    counter += 1
    return o

o = ''
for i in range(45):
    nextnumber()
    nextnumber()
    s = get2bytes()
    o += chr(s >> 8) + chr(s & 0xff)

print(o)
