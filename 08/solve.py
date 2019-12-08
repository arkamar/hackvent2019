#! /bin/env python

def double(n):
    n = n * 2
    if n >= 10:
        n = n % 10 + 1
    return n

def luhn(n):
    i = 0
    s = 0
    while n:
        r = n % 10
        if i % 2:
            s += double(r)
        else:
            s += r
        n = n // 10
        i += 1
    return s

def decode(s):
    s = s[2:]
    o = ''
    for i in range(len(s)):
        o += chr(ord(s[i]) - 30 - i)
    return o

m = (
    ':)QVXSZUVY\ZYYZ[a',
    ':)QOUW[VT^VY]bZ_',
    ':)SPPVSSYVV\YY_\\\\]',
    ':)RPQRSTUVWXYZ[\]^',
    ':)QTVWRSVUXW[_Z`\\b',
    ':)SlQRUPXWVo\\Vuv_n_\\ajjce'
)

for i in m[:-1]:
    n = decode(i)
    print(n, luhn(int(n)))

print('HV19{' + decode(m[-1]) + '}')
