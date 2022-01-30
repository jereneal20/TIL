# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p == root or q == root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.getPath(root, p, [])
        q_path = self.getPath(root, q, [])

        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            i += 1
        return p_path[i - 1]

    def getPath(self, node, target, path):
        if not node:
            return []

        if node == target:
            return path + [node]

        return self.getPath(node.left, target, path + [node]) + self.getPath(node.right, target, path + [node])
