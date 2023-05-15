"""
GRID GRAPH
Given a 2d array of size n * n made up of Land (1) and water (0), return the amount of distinct islands.
An island in this context is a vertical or horizontal connected region of land.
Assume the area outside the array is water.

. 0 . . 0 .
0 0 . . 0 .
. 0 . . . .
. . . 0 0 .
. 0 . 0 0 .
. . . . . .
answer = 4 because there are 4 distinct islands
"""


grid = [
[0, 1, 0, 0, 1, 0,],
[1, 1, 0, 0, 1, 0,],
[0, 1, 0, 0, 0, 0,],
[0, 0, 0, 1, 1, 0,],
[0, 1, 0, 1, 1, 0,],
[0, 0, 0, 0, 0, 0,],
]

def island_count(grid):
    """
    PLAN:
    - Iteratively traverse to ensure it checked every spot (nested for loop)
    - If it encounters an island, start bfs, keeping track of visited nodes
    - when exhausted all neighbors, increment island count by 1
    * Each node is a grid location (row, col) with (0,0) being the top left corner
    """
    # adding a border around the grid
    grid.insert(0, [0 for _ in grid[0]])
    grid.append([0 for _ in grid[0]])
    for row in grid:
        row.insert(0, 0)
        row.append(0)
    
    # for row in grid:
    #     print(row)

    visited = set()
    count = 0
    for row in range(1, len(grid)-2):
        for col in range(1, len(grid[row])-2):
            if (row, col) in visited:
                continue
            if grid[row][col] == 1: # if it's an island, start the bfs
                # print('island')
                queue = [(row, col)]
                while len(queue) > 0: # while there's still something in the queue
                    # unpack the first coordinates from the queue.
                    curr_row, curr_col = queue.pop(0)
                    if (curr_row, curr_col) in visited or grid[curr_row][curr_col] == 0:
                        continue
                    visited.add((curr_row,curr_col))
                    
                    queue.append((curr_row - 1, curr_col))
                    queue.append((curr_row + 1, curr_col))
                    queue.append((curr_row, curr_col - 1))
                    queue.append((curr_row, curr_col + 1))
                count += 1

    # for row in grid:
    #     print(row)
    return count


print(island_count(grid))