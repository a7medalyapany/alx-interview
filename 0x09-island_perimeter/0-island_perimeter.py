#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    
    Args:
        grid (List[List[int]]): A 2D grid where 1 represents land and 0 represents water.
    
    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with 4 potential sides
                sides = 4
                
                # Check top side
                if r > 0 and grid[r - 1][c] == 1:
                    sides -= 1
                
                # Check bottom side
                if r < rows - 1 and grid[r + 1][c] == 1:
                    sides -= 1
                
                # Check left side
                if c > 0 and grid[r][c - 1] == 1:
                    sides -= 1
                
                # Check right side
                if c < cols - 1 
