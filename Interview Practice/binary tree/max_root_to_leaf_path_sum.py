"""
Given the root of a binary tree,
return the largest sum of numbers you can get by traversing from root to any leaf.
       5
      / \
    11   3
   /  \   \
  4   15   12
answer: 31 because 5 + 11 + 15
"""
import tree_varied_nums as tr

def max_path_sum(root):
    # PLAN:
    # dfs, in the stack keep the current node (starts with root)
    # and also the current sum (starts with root value)
    # if you reach a leaf, check if you should replace the current high score with curr sum
    result = 0
    stack = [(root, root.val)] # tuple of current node and sum
    while len(stack) > 0:
        curr, sum = stack.pop() # unpack the tuple
        if curr == None: # skip
            continue
        if not curr.left and not curr.right: # if it is a leaf (no children)
            if sum > result:
                result = sum
        else: # might as well only check these if we know at least one exists
            stack.append((curr.left, sum + curr.val))
            stack.append((curr.right, sum + curr.val))
    return result

print(max_path_sum(tr.a))