#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # get the absolute value of the number and its last digit
    print(last_digit, end="")
    return last_digit

