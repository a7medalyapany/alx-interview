#!/usr/bin/python3
"""
Rotate 2D Matrix Module
"""

def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix by 90 degrees clockwise in place.
    Args:
    matrix (list of list of int): The matrix to rotate.
    
    Returns:
    None
    """
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    rotate_2d_matrix(matrix)
    print(matrix)
