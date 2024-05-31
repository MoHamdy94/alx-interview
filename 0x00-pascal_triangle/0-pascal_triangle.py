#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # Start with the first element as 1
        for j in range(1, i):
            # Each interior element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End with the last element as 1
        triangle.append(row)
    return triangle
