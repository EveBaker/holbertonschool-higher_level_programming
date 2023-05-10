#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    valid_names = [name for name in names if not name.startswith('__')]
    valid_names.sort()
    for name in valid_names:
        print(name)
