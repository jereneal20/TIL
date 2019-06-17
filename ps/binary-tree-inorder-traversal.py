# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = list()
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = list()
        self.inorderTraversals(root)
        return self.res
    
    def inorderTraversals(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.inorderTraversals(root.left)
        self.res.append(root.val)
        self.inorderTraversals(root.right)
        
