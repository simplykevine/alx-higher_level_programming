#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(i) if i % 2 == 0 else chr(i-32), end='')
