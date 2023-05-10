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
        for x in graph[curr]:
            stack.append(x)
    return



depth_print(graph, 'a')