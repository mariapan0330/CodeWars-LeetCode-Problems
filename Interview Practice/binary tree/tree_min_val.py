"""
Given the root of a binary tree, return the smallest number in the tree.
       5
      / \
    11   3
   /  \   \
  4   15   12
answer: 3
"""
import tree_varied_nums as tree

def tree_min_val(root):
    # PLAN: 
    # - DFS - let's do recursively because I'm bad at that
    # - keep track of the high score
    if root == None:
        return float('inf')
    return min(root.val, tree_min_val(root.left), tree_min_val(root.right))


print(tree_min_val(tree.a))
