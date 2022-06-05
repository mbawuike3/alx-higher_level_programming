#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            hr_sp = 0
            for j in i:
                if hr_sp != 0:
                    print(" ", end='')
                hr_sp = 1
                print("{:d}".format(j), end='')
            print("")
