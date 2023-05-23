"""
Given the root of a binary tree, print all the values according to a breadth first traversal.
      a
     / \
    b   c
   / \   \
  d   e   f

BFS looks at each node evenly (instead of following one path to the end), so result is ABCDEF
PLAN: Implement a queue (first in, first out)
- while there's something on the queue:
    - the end thing in the queue gets popped and becomes current value
    - if it is null, stop there
    - else, print it out and add its left and right vals to the start of the queue
TIME: O(n) where n = # nodes
SPACE: O(n) where n = # nodes
"""

import node_class

def bfs_binary_tree(root):
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop()
        if curr == None:
            continue
        print(curr.val)
        queue.insert(0, curr.left)
        queue.insert(0, curr.right)

bfs_binary_tree(node_class.a)