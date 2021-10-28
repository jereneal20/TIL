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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidTree(root.val, pow(2, 31), root.right) and self.isValidTree(-pow(2, 31) - 1, root.val, root.left)

    def isValidTree(self, leftMost, rightLeast, node):
        if node == None:
            return True
        if node.val <= leftMost or rightLeast <= node.val:
            return False
        return self.isValidTree(node.val, rightLeast, node.right) and self.isValidTree(leftMost, node.val, node.left)


