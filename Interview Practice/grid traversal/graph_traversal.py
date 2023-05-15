# GRAPH TRAVERSAL
# tree and matrix traversal
# depth-first search and breadth-first search
# traverse through cyclic graphs

# arrow symbols found at https://en.wikipedia.org/wiki/Arrow_(symbol)
# ↓ ↑ ← → 
# following the lesson https://www.youtube.com/watch?v=tWVWeAqZ0WU

"""
===== DEPTH-FIRST TRAVERSAL =====
Example graph:
a → c
↓   ↓
b   e
↓
d → f
"""

graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

# GOAL = traverse through and print out the whole graph using depth-first search
# PLAN:
# - Stack method (first in, first out)
# - put the source on the stack
# - while there's still something on the stack, pop the ending thing out of the stack
# - that's the current one
# - print the current one
# - if it has neighbors, put the neighbors on the stack.

def depth_print(graph, source): # source is the node you're starting the search at
    curr = 0
    stack = [source]
    while stack:
        curr = stack.pop()
        print(curr)
        for x in graph[curr][::-1]:
            stack.append(x)
    return

def depth_print_recursive(graph, curr):
    print(curr)
    for x in graph[curr]:
        # base case is that the current node has no neighbors (then the recursion doesn't continue)
        depth_print_recursive(graph, x)
    return

print("depth")
depth_print(graph, 'a')
print("depth + recursive")
depth_print_recursive(graph, 'a')

def breadth_print(graph, source):
    # queue method
    # plan:
    # queue initialized containing the source
    # while there's stuff in the queue:
        # curr node is the popped END of the queue
        # print curr node
        # curr node's neighbors are put into the FRONT of the queue
    queue = [source]
    curr = 0
    while queue != []:
        curr = queue.pop()
        print(curr)
        for node in graph[curr]:
            queue.insert(0, node)

print('breadth')
breadth_print(graph, 'a')