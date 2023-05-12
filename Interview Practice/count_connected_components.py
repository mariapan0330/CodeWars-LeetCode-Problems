"""
Given an undirected graph, return the number of connected components.
1 - 2   3

    4
    |
5 - 6 - 8
    |
    7
"""

graph = {
    1: [2],
    2: [1],
    3: [],
    4: [6],
    5: [6],
    6: [4,5,7,8],
    7: [6],
    8: [6],
}

def count_connected_components(graph):
    count = 0
    visited = set()
    # print(graph)  
    for node in graph:
        if node in visited:
            continue
        stack = [node]
        curr = None
        while len(stack) > 0:
            curr = stack.pop()
            visited.add(curr)
            for n in graph[curr]:
                if n not in visited:
                    stack.append(n)
        else:
            count += 1

    return count


print(count_connected_components(graph))