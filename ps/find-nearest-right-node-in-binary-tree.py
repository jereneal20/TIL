# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        deq = deque([(root, 0)])
        while deq:
            node, depth = deq.popleft()
            if node == u:
                if deq and deq[0][1] == depth:
                    return deq[0][0]
                else:
                    return None
            if node.left:
                deq.append((node.left, depth + 1))
            if node.right:
                deq.append((node.right, depth + 1))
        return None
