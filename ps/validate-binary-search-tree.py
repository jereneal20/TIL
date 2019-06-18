# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.recurse(root, -sys.maxsize, sys.maxsize)
    
    def recurse(self, node, L, R):
        if not node:
            return True
        if node.val >= R or node.val <= L:
            return False
        return self.recurse(node.left, L, node.val) and self.recurse(node.right, node.val, R)
