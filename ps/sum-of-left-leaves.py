# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if self.is_leaf(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        if self.is_leaf(root.right):
            return self.sumOfLeftLeaves(root.left)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def is_leaf(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        return False
