"""
Given the root of a binary tree, do a depth first traversal and print out every value in the tree

      a
     / \
    b   c
   / \   \
  d   e   f

DFS makes you go to the deepest parts first, so it will print out ABDECF

PLAN:
- implement a stack; first in last out
- start with the root node A on the stack
- while the stack isn't empty:
    - pop the top thing from the stack, mark as current
    - mark curr as visited
    - add the left and right children of this node to stack

TIME: O(n) where n is number of nodes
SPACE: O(n) where n is number of nodes
"""
import node_class

def dfs_values(root):
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        if curr == None:
            continue

        print(curr.val)

        stack.append(curr.right)
        stack.append(curr.left)


dfs_values(node_class.a)