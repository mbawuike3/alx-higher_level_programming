#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    kyl = 0
    for i in range(1, argc):
        kyl = kyl + int(sys.argv[i])
    print("{:d}".format(kyl))
