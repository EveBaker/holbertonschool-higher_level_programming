#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

# Testing the function
test_cases = [
    ([1, 2, 3], 1),
    ([1, 2, 3], 0),
    ([1, 2, 3], 2),
    ([1, 2, 3], 3),
    ([1, 2, 3], -1),
    ([1], 0),
    ([1], 1)
]

for lst, idx in test_cases:
    print(f"List: {lst}, Index: {idx} => Element: {element_at(lst, idx)}")