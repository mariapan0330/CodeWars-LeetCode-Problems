"""
Given an m x n 2d binary grid which represents a map of 1s (land) and 0s (water), return the number of islands

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

1 1 1 1 .
1 1 . 1 .
1 1 . . .
. . . . .
output = 1

1 1 . . .
1 1 . . .
. . 1 . .
. . . 1 1
output = 3
"""

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

def num_islands(grid):
    """
    Plan: BFS and node tracking
    - Go through all items in all lists
    - if you have visited it before, skip. If water, skip.
    - keep an island count
    - otherwise it must be uncharted land, in which case: BFS
        - keep a queue where the first item is the current node's **coordinates**
        - while there is still something in the queue:
            - pop the last thing off the queue
            - if it's out of bounds, skip
            - if it's visited, skip
            - if it is unvisited, mark as visited and continue
            - add neighbors to the queue. Neighbors are vert and horiz coordinates (x + 1, x - 1, y + 1, y - 1)
            - if there's nothing left on the queue, then you've visited the whole island. Increment the island count by 1.
    """

    visited = set()
    island_count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (i,j) in visited or grid[i][j] == "0":
                continue
            queue = [(i, j)]
            while len(queue) > 0:
                x, y = queue.pop()
                # print(curr_x, curr_y)
                if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                    continue
                if (x,y) in visited or grid[x][y] == "0":
                    continue

                visited.add((x,y))
                print(x, y, "is part of an island")
                queue.insert(0, (x + 1, y))
                queue.insert(0, (x - 1, y))
                queue.insert(0, (x, y + 1))
                queue.insert(0, (x, y - 1))
            print('end')
            island_count += 1
    return island_count


# print(num_islands(grid))
print(num_islands(grid2))