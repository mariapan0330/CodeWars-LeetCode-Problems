def path_finder(maze):
    queue = [""]
    path = ""

    # while you have not reached the end
    # set path var to the first item in the queue
    # for each possible direction, 
    # if it's a valid direction to add to the path,
    # add it onto the path and put that in the queue.
    flag = False
    print("=== MAZE ===")
    maze = maze.split("\n")
    print(maze)
    print("=====")
    
    count = 0

    while not found_end(maze, path) and count < 10:
        if len(queue) == 0:
            return False
        path = queue.pop(0)
        count_tries = 0
        for dir in ["N","S","E","W"]:
            possibility = path + dir
            if is_valid(maze, possibility):
                print('valid')
                queue.append(possibility)
                # print(queue)
        # else:
            # if none of the possibilities were valid moves, stop the loop bc it failed.
            # return False
        # flag = True
        count += 1

    return queue


def is_valid(maze, path):
    print("Now testing", path)
    x = 0
    y = 0
    for i, move in enumerate(path):
        if move == "N":
            if x-1 < 0:
                return False
            if maze[x-1][y] == "W":
                return False
            if len(path) > 3 and path[i-2] == "N":
                return False
            x -= 1

        if move == "S":
            print(x+1, y)
            if x+1 > len(maze)-1:
                return False
            if maze[x+1][y] == "W":
                return False
            if len(path) >= 3 and path[i-2] == "S":
                print("FLAG")
                return False
            x += 1


        if move == "W": # left
            if y-1 < 0:
                return False
            if maze[x][y-1] == "W":
                return False
            if len(path) > 3 and path[i-2] == "W":
                return False
            y -= 1
            

        if move == "E":
            if y+1 > len(maze)-1:
                return False
            if maze[x][y+1] == "W":
                return False
            if len(path) > 3 and path[i-2] == "E":
                return False
            y += 1

    return True


def found_end(maze, path):
    x = 0
    y = 0
    for i, move in enumerate(path):
        if move == "N":
            x -= 1
        
        elif move == "S":
            x += 1
        
        elif move == "E":
            y += 1
        
        elif move == "W":
            y -= 1
    
    if x == len(maze)-1 and y == len(maze)-1:
        print("found!")
        return True
    
    return False


# starting at position [0,0] (top left), return the length of the 
# shortest path to [N-1,N-1] (bottom left) if W represents an impassable wall.
# return False if it is impossible to reach the exit from the starting point.

maze1 = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

maze2 = "\n".join([
  ".W.",
  ".W.",
  "..."
])

maze3 = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])


print(path_finder(maze2))