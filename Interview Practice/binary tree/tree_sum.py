"""
Given a b.tree root, return the sum of everything in the tree
      1
     / \
    2   3
   / \   \
  4   5   6
OUTPUT: 21
WHY: 1 + 2 + 3 + 4 + 5 + 6 = 21
"""

import node_class_numbers

def tree_sum(root):
    stack = [root]
    total = 0
    while len(stack) > 0:
        curr = stack.pop()
        if curr == None:
            continue
        total += curr.val

        stack.append(curr.left)
        stack.append(curr.right)
    return total

print(tree_sum(node_class_numbers.a))
print(tree_sum(node_class_numbers.b))


# recursive solution
"""
      1
     / \
    2   3
   / \  |\
  4   5 x 6
 / \ / \  |\
x  x x  x x x
"""

def tree_sum_r(root):
    if root == None:
        return 0
    return root.val + tree_sum_r(root.left) + tree_sum_r(root.right)

print('===')
print(tree_sum_r(node_class_numbers.a))