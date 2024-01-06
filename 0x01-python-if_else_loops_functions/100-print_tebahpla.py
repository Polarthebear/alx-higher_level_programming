#!/usr/bin/python3
for ch in range(ord('z'), ord('a') - 1, -1):
    if ch % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(ch - diff)), end='')
