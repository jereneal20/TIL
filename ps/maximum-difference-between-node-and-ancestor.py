# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, root.val, root.val)

    def recurse(self, node, max_so_far, min_so_far):
        if not node:
            return max_so_far - min_so_far
        max_so_far = max(max_so_far, node.val)
        min_so_far = min(min_so_far, node.val)

        return max(self.recurse(node.left, max_so_far, min_so_far), self.recurse(node.right, max_so_far, min_so_far),
                   max_so_far - min_so_far)


