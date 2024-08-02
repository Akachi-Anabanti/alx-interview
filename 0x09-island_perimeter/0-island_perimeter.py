#!/usr/bin/python3

'''A script that solves the island perimeter problem'''


def island_perimeter(grid):
    """calculates the perimeter of an island
    using a grid system where 0 is water and 1 is land"""

    # i and j are the current position

    # i, j # where i is used to transverse horizontally
    # j is used to transverse vertically
    # up = j + 1
    # down = j - 1
    # left = i - 1
    # right = i + 1

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check for all neighbors
                left = grid[i - 1][j] if i > 0 else 0
                right = grid[i + 1][j] if i < rows - 1 else 0
                top = grid[i][j + 1] if j < cols - 1 else 0
                bottom = grid[i][j - 1] if j > 0 else 0

                if left == 0 and right == 0 and top == 0 \
                        and bottom == 0:
                            perimeter += 4
                            return perimeter
                cell_perimeter = 4
                if left == 1:
                    cell_perimeter -= 1
                if right == 1:
                    cell_perimeter -= 1
                if top == 1:
                    cell_perimeter -= 1
                if bottom == 1:
                    cell_perimeter -= 1

                perimeter += cell_perimeter

    return perimeter
