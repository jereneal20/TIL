# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        deq = deque()
        deq.append((root, 0))

        res = [root.val]
        prev_depth = 0
        while len(deq) != 0:
            node, depth = deq.popleft()
            if not node:
                continue
            if depth > prev_depth:
                prev_depth = depth
                res.append(node.val)

            deq.append((node.right, depth + 1))
            deq.append((node.left, depth + 1))
        return res




