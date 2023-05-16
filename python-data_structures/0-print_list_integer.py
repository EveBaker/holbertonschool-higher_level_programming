#!/usr/bin/python3

def print_list_integer(my_list=[]):
        for num in my_list:
                    if type(num) == int:
                                    print("{:d}".format(num))
                                            else:
                                                            raise TypeError("List should only contain integers")

                                                            # Test cases
                                                            print_list_integer([1, 2, 3])
                                                            print_list_integer([1])
                                                            print_list_integer([])
                                                            try:
                                                                    print_list_integer([1, 2, "H", 9])
                                                            except TypeError:
                                                                    print("Exception occurred")


