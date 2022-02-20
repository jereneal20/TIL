
class TreeNode:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.val = key



def visible_nodes(root):
  def recurse(node, depth):
    if not node:
      return depth
    max_depth = max(recurse(node.left, depth + 1), recurse(node.right, depth + 1))
    return max_depth
  max_depth = recurse(root, 0)
  return max_depth
