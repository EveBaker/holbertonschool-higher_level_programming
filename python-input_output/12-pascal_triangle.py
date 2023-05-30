#!/usr/bin/python3
"""
Module: pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row [1]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        for j in range(1, i):
            # Calculate the value based on the previous row
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
