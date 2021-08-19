# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xDepth = (-1, None)
        yDepth = (-2, None)
        deq = deque([(root, 0, None)])
        while deq:
            node = deq.popleft()
            if node[0] == None:
                continue
            if node[0].val == x:
                xDepth = (node[1], node[2])
            if node[0].val == y:
                yDepth = (node[1], node[2])
            deq.append((node[0].left, node[1] + 1, node[0]))
            deq.append((node[0].right, node[1] + 1, node[0]))

        if xDepth[0] == yDepth[0] and xDepth[1] != yDepth[1]:
            return True

        return False

    def isCousins2(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root == None:
            return True

        if None not in [root.left, root.right]:
            if set((root.left.value, root.right.value)) == set((x, y)):
                return False
            self.isCousins(root.left, x, y) and self.isCousins(root.right, x, y)
            getDepth(root.left, x)
            getDepth(root.left, x)

        if root.left is None:
            return self.isCousins(root.right, x, y)
        if root.right is None:
            return self.isCousins(root.left, x, y)
        if set((root.left, root.right)) == set((x, y)):
            return False
        return self.isCousins(root.left, x, y) and self.isCousins(root.right, x, y)

    def getDepth(self, root, x):
        if root == None:
            return -200
        if root.value == x:
            return 1
        return max(getDepth(root.left), getDepth(root.right)) + 1