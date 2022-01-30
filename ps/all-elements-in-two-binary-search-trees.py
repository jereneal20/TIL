# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        ans = []
        inorder(root1)
        ans2 = ans
        ans = []
        inorder(root2)

        i, j = 0, 0
        res = []
        while i < len(ans) and j < len(ans2):
            if ans[i] < ans2[j]:
                res.append(ans[i])
                i += 1
            else:
                res.append(ans2[j])
                j += 1

        if i == len(ans):
            res.extend(ans2[j:])
        elif j == len(ans2):
            res.extend(ans[i:])

        return res