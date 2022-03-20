# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        root.left = left
        root.right = right
        return root


