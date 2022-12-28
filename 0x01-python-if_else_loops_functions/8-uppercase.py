#!/usr/bin/python3
def uppercase(str):
    lent = len(str)
    for i in range(lent):
        c = ord(str[i])
        if c >= 97 and c <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(c - num), end='')
    print()
