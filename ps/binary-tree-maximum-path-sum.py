# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = self.recursion(root)
        return res[1]
    
    def recursion(self, node):
        if not node:
            return -sys.maxsize, -sys.maxsize
        l = self.recursion(node.left)
        r = self.recursion(node.right)
        return max(node.val+l[0],node.val+r[0],node.val), max(r[1], l[1], r[0]+l[0]+node.val, r[0]+node.val,l[0]+node.val,node.val)
