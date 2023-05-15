"""
Same as "shortest_path" but I challenged myself to return the sequence instead of just path length.

Given a list of edges, a start node, and an end node,
return the shortest path between Start and End, or return -1 if no path is found.
1 - 2 - 3
  \    /
  5 - 4

  6 - 7

"""

edges = [
    [1,2],
    [2,3],
    [3,4],
    [4,5],
    [5,1],
    [6,7]
]


def shortest_path(edges, start, end):
    """
    Plan: BFS
    - in the queue, keep track of the current seq too
    - while there's still something in the queue, make the first thing in q the current node
    and check if that's the goal node.
        - If not, add this one's neighbors to end of queue.
    - because it's an undirected graph, keep track of visited nodes.
    """
    graph = make_graph(edges)
    # print(graph)
    
    queue = [([start], start)] # [current sequence], current node
    visited = {start}
    while len(queue) > 0:
        curr_seq, curr = queue.pop(0)
        visited.add(curr)
        if curr == end:
            return curr_seq
        
        for neighbor in graph[curr]:
            if neighbor not in visited:
                queue.append((curr_seq + [neighbor], neighbor))
    return -1

def make_graph(edges):
    graph = dict()
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]] += [edge[1]]
        graph[edge[1]] += [edge[0]]
    return graph


print(shortest_path(edges, 1, 4))
print(shortest_path(edges, 1, 6))
print(shortest_path(edges, 1, 3))
print(shortest_path(edges, 2, 3))
print(shortest_path(edges, 6, 7))