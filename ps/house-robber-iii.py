# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.map = {}
        return self.maximum_amount(root)

    def maximum_amount(self, node):
        ret = 0
        if not node:
            return 0
        if node in self.map:
            return self.map[node]

        if node.left:
            ret += self.maximum_amount(node.left.left) + self.maximum_amount(node.left.right)

        if node.right:
            ret += self.maximum_amount(node.right.left) + self.maximum_amount(node.right.right)

        ret = max(ret + node.val, self.maximum_amount(node.left) + self.maximum_amount(node.right))
        self.map[node] = ret
        return ret
