#!/usr/bin/python3
"""Module for minimum operations on an input"""


def minOperations(n):
    """
    Gets the fewest number of operation
    to have same number of characters as input
    """
    # Output should be at least two characters
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
