#!/usr/bin/python3    
def uppercase(str):
    for c in str:
        ascii_code = ord(c)
    if 97 <= ascii_code <= 122:
        uppercase_code = ascii_code - 32
        print("{:c}".format(uppercase_code), end="")
    else:
        print("{:c}".format(ascii_code), end="")
        print()

