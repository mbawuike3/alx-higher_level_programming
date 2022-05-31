#!/usr/bin/python3
num = 1
for k in range(122, 96, -1):
    if(num % 2 == 0):
        j = k - 32
    else:
        j = k
    print("{:s}".format(chr(j)), end="")
    num += 1
