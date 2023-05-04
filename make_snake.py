"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""

"""
    PLAN:
    - Make a grid the same l and w as size param, filled with 0s
    - fill the first line with 1s and put 1s at the end of every line
    - flip the list horizontally and vertically, subtract 2 from size and make it go again  
"""

spiral = []
def spiralize(size):

    # for each num until size, add a new line into the spiral filled with as many 0s as size
    for x in range(0,size): 
        spiral.append([0 for i in range(0,size)])
    go_spiral(size)
    return spiral

def go_spiral(size):
    # make the first line all 1s.
    # print(len(spiral), size)
    # spiral[len(spiral)-size] = [1 for i in range(0,size)]
    for x in range(len(spiral)-size,len(spiral)):
        spiral[0][x] = 2

    # for each num until size, add a 1 to the end of the line.
    for x in range(0,size):
        if x == 0:
            continue
        spiral[x][-1] = 1
    
    # set the corner of the next square to 1
    spiral[size-1][-2] = 3

    print("~~~~~ size:", size)
    for x in spiral:
        print(x)
    print("~~~~~")

    spiral.reverse()
    print("Flipped:")
    for x in range(0,len(spiral)):
        spiral[x].reverse()
        print(spiral[x])
    print("end flipped")
    size -= 2
    if size > 0:
        go_spiral(size)

spiral = spiralize(7)
print("=== FINAL ===")
for line in spiral:
    print(line)