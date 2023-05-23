"""
Given a binary tree root and a target value,
return True if the value exists within the tree and False if not.
      a
     / \
    b   c
   / \   \
  d   e   f
target = e
OUTPUT: True

target = j
OUTPUT: False
"""

import node_class

def tree_includes(root, target):
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop()
        if curr == None:
            continue

        if curr.val == target:
            return True
        queue.insert(0, curr.left)
        queue.insert(0, curr.right)
    return False

print(tree_includes(None, 'e')) # false
print(tree_includes(node_class.a, 'e')) # true
print(tree_includes(node_class.a, 'j')) # false
print(tree_includes(node_class.b, 'f')) # false
print(tree_includes(node_class.b, 'e')) # true

def tree_includes_but_recursive(root, target):
    if root == None:
        return False
    if root.val == target:
        return True

    left = tree_includes_but_recursive(root.left, target)
    right = tree_includes_but_recursive(root.right, target)

    return left or right

print("===")
print(tree_includes_but_recursive(None, 'e')) # false
print(tree_includes_but_recursive(node_class.a, 'e')) # true
print(tree_includes_but_recursive(node_class.a, 'j')) # false
print(tree_includes_but_recursive(node_class.b, 'e')) # true
