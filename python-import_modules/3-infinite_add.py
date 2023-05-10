#!/usr/bin/python3
import sys

def infinite_add():
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)

if __name__ == "__main__":
    infinite_add()
