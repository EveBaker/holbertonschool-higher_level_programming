#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper_char = chr(ord(c) - ord('a') + ord('A'))
        else:
            upper_char = c
        print("{:s}".format(upper_char), end="")
    print()

