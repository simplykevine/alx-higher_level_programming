#!/usr/bin/python3
for numb in range(00, 100):
    if numb < 99:
        print("{:02d}, ".format(numb), end="")
    else:
        print("{:02d}".format(numb))
