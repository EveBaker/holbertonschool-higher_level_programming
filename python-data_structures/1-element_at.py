#!/usr/bin/python3

def element_at(my_list, idx):
        if idx < 0 or idx >= len(my_list):
                    return None
                    return my_list[idx]

                # Test cases
                print(element_at([1, 2, 3], 3))  # Correct output: None
                print(element_at([1, 2, 3], -1))  # Correct output: None
                print(element_at([1], 0))  # Correct output: 1
                print(element_at([1], 1))  # Correct output: None
