"""
Given a list of edges, a start node, and an end node,
return the shortest path between Start and End
1 - 2 - 3
  \    /
  5 - 4

"""

edges = [
    [1,2],
    [2,3],
    [4,5],
    [5,1],
    [3,4],
]

def shortest_path(edges, start, end):
    # plan: dfs (stack)
    # keep count of current sequence length
    # keep high score (result) of shortest found length
    graph = make_graph(edges)
    curr_seq = []
    result = edges[:]
    # print(graph)

    stack = [start]
    curr = None
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        visited.add(curr)
        curr_seq.append(curr)
        if curr == end:
            if len(curr_seq) < len(result):
                result = curr_seq[:]
                curr_seq = []
                print("found path", result)
        for node in graph[curr]:
            if node not in visited:
                stack.append(node) 
    return result


def shortest_path(edges, start, end):
    """ PLAN: BFS, and keep track of visited bc it's non-directional.
    Also keep track of the length of the combo - as you add nodes onto the queue,
    increment the path length to take that particular paath.
    """
    graph = make_graph(edges)
    q = [(start, 0)] # initialize queue with start node and length of current pattern
    curr = None
    result = len(edges)
    visited = set()
    while len(q) > 0:
        curr, length = q.pop()
        visited.add(curr)
        if curr == end:
            if length < result:
                result = length
        for node in graph[curr]:
            if node not in visited and node not in q:
                q.insert(0, (node, length + 1))
    return result




def make_graph(edges):
    graph = dict()
    for edge in edges:
        x,y = edge
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x] += [y]
        graph[y] += [x]
    return graph

print(shortest_path(edges, 1, 4))
print(shortest_path(edges, 1, 3))
print(shortest_path(edges, 1, 2))