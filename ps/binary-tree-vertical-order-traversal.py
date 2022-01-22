# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        que.append((root, 0))
        self.mp = {}

        while len(que) != 0:
            node, index = que.popleft()
            if not node:
                continue
            if index not in self.mp:
                self.mp[index] = []
            self.mp[index].append(node.val)

            que.append((node.left, index - 1))
            que.append((node.right, index + 1))

        res = []
        indices = sorted(self.mp)
        for i in indices:
            res.append(self.mp[i])
        return res