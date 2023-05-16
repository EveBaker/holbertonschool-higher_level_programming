#!/usr/bin/python3

def print_list_integer(my_list=[]):
        for num in my_list:
                    if type(num) is not int:
                                    raise TypeError("list must contain only integers")
                                        print("{:d}".format(num))

                                        # Test cases
                                        try:
                                                my_list = [1, 2, 3]
                                                    print_list_integer(my_list)
                                                        # Output: 1
                                                            #         2
                                                                #         3

                                                                    my_list = [1]
                                                                        print_list_integer(my_list)
                                                                            # Output: 1

                                                                                my_list = []
                                                                                    print_list_integer(my_list)
                                                                                        # No output

                                                                                            my_list = [1, 2, "H", 9]
                                                                                                print_list_integer(my_list)
                                                                                                    # Output: TypeError: list must contain only integers
                                        except TypeError as error:
                                                print(error)

