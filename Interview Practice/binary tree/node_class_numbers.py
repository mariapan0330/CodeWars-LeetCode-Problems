class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

"""
The above sets up a binary tree
      1
     / \
    2   3
   / \   \
  4   5   6
"""