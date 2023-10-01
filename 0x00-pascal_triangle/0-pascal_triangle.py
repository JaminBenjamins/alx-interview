#!/usr/bin/python3
"""
    A function that returns the Pascal's Triangle
"""


def pascal_triangle(n):
    """
        Return a nested list of integers
        that represents the Pascal's triangle
        Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
