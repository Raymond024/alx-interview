#!/usr/bin/python3
"""Island Perimeter
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    peri = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if (grid[x][y] == 1):
                if (x <= 0 or grid[x - 1][y] == 0):
                    peri += 1
                if (x >= len(grid) - 1 or grid[x + 1][y] == 0):
                    peri += 1
                if (y <= 0 or grid[x][y - 1] == 0):
                    peri += 1
                if (y >= len(grid[x]) - 1 or grid[x][y + 1] == 0):
                    peri += 1
    return peri
