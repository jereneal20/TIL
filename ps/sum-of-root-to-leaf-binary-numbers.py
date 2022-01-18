# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.recurse(root, [])
        return self.res

    def recurse(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            self.res += int(''.join(path + [str(node.val)]), 2)
            return

        self.recurse(node.left, path + [str(node.val)])
        self.recurse(node.right, path + [str(node.val)])
        return