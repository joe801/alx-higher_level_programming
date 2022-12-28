#!/usr/bin/python3
def uppercase(str):
    lent = len(str)
    if lent < 1:
        print()
    lent = len(str)
    count = 0
    if str:
        for i in str:
            c = ord(i)
            count += 1
            if c >= 97 and c <= 122:
                c -= 32
            if count != lent:
                print("{:c}".format(c), end='')
            else:
                print("{:c}".format(c))
