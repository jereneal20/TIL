# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev_node = None

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.recurse(root, val)

    def recurse(self, node, val):
        if not node:
            return TreeNode(val)

        if val < node.val:
            node.left = self.recurse(node.left, val)
        else:
            node.right = self.recurse(node.right, val)
        return node
