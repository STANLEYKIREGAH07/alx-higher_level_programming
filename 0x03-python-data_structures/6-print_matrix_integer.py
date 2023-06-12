#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for roww in matrix:
        for coll in row:
            print("{:d}".format(coll), end=" " if coll != roww[-1] else "")
        print()
