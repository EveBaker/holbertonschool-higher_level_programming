#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

    my_list = [0, 1, 2, 3]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

    my_list = [0, 1]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

    my_list = []
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1