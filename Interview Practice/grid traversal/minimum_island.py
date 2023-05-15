"""
Given a 2d array grid of size n * m filled with water (0) and land (1),
return the size of the smallest island on the grid.
An island is a land mass that is connected vertically or horizontally.
An island in this context is a vertical or horizontal connected region of land.
Assume the area outside the array is water.

. 0 . . 0 .
0 0 . . 0 .
. 0 . . . .
. . . 0 0 .
. . . 0 0 .
. . . 0 . .
answer = 2 because the smallest island is 2 blocks large
"""

grid = [
[0, 1, 0, 0, 1, 0,],
[1, 1, 0, 0, 1, 0,],
[0, 1, 0, 0, 0, 0,],
[0, 0, 0, 1, 1, 0,],
[0, 0, 0, 1, 1, 0,],
[0, 0, 0, 1, 0, 0,],
]

seen_grid = [
[7, 7, 7, 7, 7, 7],
[7, 7, 7, 7, 7, 7],
[7, 7, 7, 7, 7, 7],
[7, 7, 7, 7, 7, 7],
[7, 7, 7, 7, 7, 7],
[7, 7, 7, 7, 7, 7],
]

def minimum_island(grid):
    """
    PLAN: 
    - go through each node in the graph (for r in grid, for c in r)
    - if water, skip
    - if land, start a bfs where each node is (r,c)
        - undirected graph = keep track of visited nodes
        - in the queue, track also the size of the current island
        - when you reach the end of the queue, check the size against the current high score
    """

    visited = set()
    # result = [len(grid[0]) * len(grid)]
    result = len(grid[0]) * len(grid)
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if (r,c) in visited:
                continue
            if grid[r][c] == 0:
                seen_grid[r][c] = '.'
                continue
            else:
                queue = [(0, r, c)]
                size = 0
                while len(queue) > 0:
                    curr_size, curr_r, curr_c = queue.pop(0)

                    inbound_row = curr_r >= 0 and curr_r < len(grid)
                    inbound_col = curr_c >= 0 and curr_c < len(grid[0])
                    if inbound_row == False or inbound_col == False:
                        continue

                    if (curr_r, curr_c) in visited or grid[curr_r][curr_c] == 0:
                        continue
                    seen_grid[curr_r][curr_c] = 0

                    visited.add((curr_r, curr_c))
                    size += 1
                    # size = curr_size

                    queue.append((curr_size+1, curr_r+1, curr_c))
                    queue.append((curr_size+1, curr_r-1, curr_c))
                    queue.append((curr_size+1, curr_r, curr_c+1))
                    queue.append((curr_size+1, curr_r, curr_c-1))
                if size < result:
                    result = size
                # result.append(size)
    for x in seen_grid:
        for y in x:
            print(y, end=' ')
        print('')
    # return min(result)
    return result


print(minimum_island(grid))