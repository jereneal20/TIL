# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        sum = 0
        if L <= root.val and root.val <= R:
            sum += root.val
        if not (root.val < L):
            # do left side
            sum += self.rangeSumBST(root.left, L, R)
        if not (R < root.val):
            # do right side
            sum += self.rangeSumBST(root.right, L, R)
        return sum


def recursive_traverse(node, L, R):
    if not node:
        return 0

    if node.val < L:
        return recursive_traverse(node.right, L, R)
    if node.val > R:
        return recursive_traverse(node.left, L, R)
	
    return node.val + recursive_traverse(node.left, L, R) + recursive_traverse(node.right, L, R)

