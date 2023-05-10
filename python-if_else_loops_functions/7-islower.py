#!/usr/bin/python3
def islower(c):
    ascii_code = ord(c)
    if 97 <= ascii_code <= 122:  # lowercase letter
        return True
    else:
        return False
