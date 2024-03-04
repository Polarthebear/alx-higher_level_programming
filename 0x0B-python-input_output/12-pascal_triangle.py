#!/usr/bin/python3
"""Function that defines a function of Pascal's Triangle."""


def pascal_triangle(n):
    """representing Pascal's Triangle of size (n).

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        triangles = tri[-1]
        tmp = [1]
        for i in range(len(triangles) - 1):
            tmp.append(triangles[i] + tri[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return triangles
