#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord(letters) >= 97 and ord(letters) <= 122:
            letters = ord(letters) - 32
        else:
            letters = ord(letters)
        print("{:c}".format(letters), end="")
    print("")
