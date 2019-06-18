# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @staticmethod
    def recurse(node):
        if not node:
            return 0, 0
        left = Solution.recurse(node.left)
        right = Solution.recurse(node.right)
        
        return max(left[0],right[0]) + 1, max(left[1], right[1], left[0]+right[0])
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.recurse(root)[1]
