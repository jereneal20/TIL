# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = list()
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = list()
        self.inorderTraversals(root)
        return self.res
    
    def inorderTraversals(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.inorderTraversals(root.left)
        self.res.append(root.val)
        self.inorderTraversals(root.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.helper(root)
        return self.result

    def helper(self, node):
        if node == None:
            return
        self.helper(node.left)
        self.result.append(node.val)
        self.helper(node.right)


        
