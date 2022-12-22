#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    count = 0
    for i in str:
        c = ord(i)
        count += 1
        if c >= 97 and c <= 122:
            c -= 32
        if count != l:
            print("{:c}".format(c), end='')
        else:
            print("{:c}".format(c))
