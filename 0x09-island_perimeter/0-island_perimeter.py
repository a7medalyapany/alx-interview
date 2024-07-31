#!/usr/bin/python3

def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    def is_water_or_out_of_bounds(r, c):
        """Helper function to check if cell is water or out of bounds"""
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return True
        return grid[r][c] == 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check each side
                if is_water_or_out_of_bounds(r - 1, c):  # Top
                    perimeter += 1
                if is_water_or_out_of_bounds(r + 1, c):  # Bottom
                    perimeter += 1
                if is_water_or_out_of_bounds(r, c - 1):  # Left
                    perimeter += 1
                if is_water_or_out_of_bounds(r, c + 1):  # Right
                    perimeter += 1

    return perimeter
