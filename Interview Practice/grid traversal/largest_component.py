"""
Given a non-directional graph, return the length of the largest component.
    5
    | \
1 - 0 - 8

4 - 2
| /
3
"""

graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[2,3],
}

def largest_component(graph):
    # keep an overall count, visited nodes, and high score (result)
    # go through each component in the graph if not visited
    # at each component, make a new stack, add current node to visited
    # and search that one's neighbors via stack method (dfs) if not visited
    result = []
    visited = set()
    for node in graph:
        # do a dfs of each node if not visited yet
        if node in visited:
            continue
        stack = [node]
        curr = None
        curr_component = []
        while len(stack) > 0:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            curr_component += [curr]

            for n in graph[curr]:
                if n not in visited:
                    stack.append(n)
        else:
            if len(curr_component) > len(result):
                result = curr_component
    return result, len(result)

res,res_len = largest_component(graph)
print(res, res_len)