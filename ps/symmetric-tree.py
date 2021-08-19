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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.func(root.left, root.right)

    def func(self, left, right):
        if (left and not right) or (right and not left):
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        return self.func(left.left, right.right) and self.func(left.right, right.left)