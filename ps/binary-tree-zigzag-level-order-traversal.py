# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = queue.Queue()
        q.put([root, 0])
        res = list()
        
        while not q.empty():
            cur = q.get()
            if not cur[0]:
                continue
            while len(res) < cur[1]+1:
                res.append([])
            res[cur[1]].append(cur[0].val)
            
            q.put([cur[0].left, cur[1]+1])
            q.put([cur[0].right, cur[1]+1])
        for idx, li in enumerate(res):
            if idx % 2 != 0:
                res[idx] = li[::-1]
        return res
            
