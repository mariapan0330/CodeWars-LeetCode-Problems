"""
Given a list of undirected neighbors, a start node, and an end node,
return True if the end node can be reached from the start node and False if it cannot. 
"""

# Time: O(edges) | Space: O(nodes)
def undirected_path(edges, start, end):
    # PLAN:
    # turn the edges into a graph
    # traverse the graph with dfs or bfs
    # If the current letter is the end letter, stop and return true
    # if you get through everything Start is connected to and don't find the End, return False
    graph = dict()

    for edge in edges:
        if edge[0] in graph and edge[1] not in graph[edge[0]]:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

        if edge[1] in graph and edge[0] not in graph[edge[1]]:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    
    stack = [start]
    curr = None
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        visited.add(curr)
        if curr == end:
            return True
        for node in graph[curr]:
            if node not in visited:
                stack.append(node)

    return False



edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n'],
    ]
"""
i - j
|
k - l
|
m

o - n
"""


edges2 = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['k','j'],
    ['o','n'],
    ]
"""
i - j
| /
k - l
|
m

o - n
"""

print(undirected_path(edges2, 'j','m'))
# print(undirected_path(edges, 'k','n'))
# print(undirected_path(edges, 'k','o'))
# print(undirected_path(edges, 'n','o'))