#!/usr/bin/python3
for numb1 in range(0, 10):
    for numb2 in range((numb1 + 1), 10):
        if (numb1 != 8) or (numb2 != 9):
            print("{}{}, ".format(numb1, numb2), end="")
        else:
            print("{}{}".format(numb1, numb2))
