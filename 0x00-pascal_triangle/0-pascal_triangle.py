#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []  # Return empty list for n <= 0

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # Start with the first element
        # Calculate the middle elements
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End with the last element
        triangle.append(row)

    return triangle

