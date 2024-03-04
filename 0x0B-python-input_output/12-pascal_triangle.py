#!/usr/bin/python3
"""Function that defines a function of Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) < n:
        last_row = tri[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        tri.append(new_row)

    return tri
