#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    totall = 0
    for x in range(len(sys.argv) - 1):
        totall += int(sys.argv[x + 1])
    print("{}".format(totall))
