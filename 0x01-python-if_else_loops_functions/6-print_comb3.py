#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and i < j and i < 8 and i < 9:
            print("{:d}".format(i), end='')
            print("{:d}, ".format(j), end='')
        if i == 8 and j == 9:
            print("{:d}".format(89))
            break
