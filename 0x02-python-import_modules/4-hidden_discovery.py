#!/usr/bin/python3

if __name__ == "__main__":
       import hidden_4

    namess = dir(hidden_4)
    for name in namess:
        if name[:2] != "__":
            print(name)
