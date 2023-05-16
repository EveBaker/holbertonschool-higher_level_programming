#!/usr/bin/python3

def print_list_integer(my_list=[]):
        for item in my_list:
                    if not isinstance(item, int):
                                    raise TypeError("All elements of the list must be integers")
                                        print("{:d}".format(item))

                                        # test cases
                                        my_list = [1, 2, 3, 4, 5]
                                        print_list_integer(my_list)

                                        my_list = [1]
                                        print_list_integer(my_list)

                                        my_list = []
                                        print_list_integer(my_list)

                                        my_list = [1, 2, "H", 9]
                                        print_list_integer(my_list)

