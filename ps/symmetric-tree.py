# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def recurse_find_sym(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    
    return recurse_find_sym(left.left, right.right) and recurse_find_sym(left.right, right.left)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
    
        return recurse_find_sym(root.left, root.right)
    

