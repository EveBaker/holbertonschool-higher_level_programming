#!/usr/bin/python3

def print_list_integer(my_list=[]):
        try:
                    for num in my_list:
                                    print("{:d}".format(num))
                                        except TypeError:
                                                    print("Exception occurred: List should only contain integers")
