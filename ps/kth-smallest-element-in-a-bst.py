# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    count = 0
    kthSmallest = -1
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.recursion(root, k)
        return self.kthSmallest
        
    def recursion(self, node, k):
        if node == None:
            return

        self.recursion(node.left, k)
        self.count += 1
        if self.count == k:
            self.kthSmallest = node.val
        self.recursion(node.right, k)
        
        return 
    
        