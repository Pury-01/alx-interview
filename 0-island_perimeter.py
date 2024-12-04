#!/usr/bin/python3
"""
function that returns the perimeter of the island described
in grid
"""


def island_perimeter(grid):
    """Calculate the perimeter of the island.

    Args:
        grid (list of list of ints): 2D grid representing the
        island and water.

    Returns:
        int: Perimeter of the island
    """

    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                # check all 4 directions
                # the top
                if row == 0 or grid[row - 1][column] == 0:
                    perimeter += 1

                # the bottom
                if row == rows - 1 or grid[row + 1][column] == 0:
                    perimeter += 1

                # right
                if column == columns - 1 or grid[row][column + 1] == 0:
                    perimeter += 1

    return perimeter
