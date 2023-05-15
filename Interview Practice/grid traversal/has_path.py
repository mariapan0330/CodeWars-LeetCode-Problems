"""
Given an acyclical & directional graph, a start node, and an end node,
check if a valid path exists from the start node to the end node.

↓ ↑ ← → ↖ ↗ ↘ ↙

EX:
f → g → h
↓ ↗
i ← j
↓
k
"""

graph = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[],
    }

def has_path(graph, start, end):
    curr = 0
    queue = [start]
    while queue != []:
        curr = queue.pop(0)
        if curr == end:
            return True
        for node in graph[curr]:
            queue.append(node)
    return False

print(has_path(graph, 'f','k'))
print(has_path(graph, 'f','j'))