"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Traverse right to left on the level is also possible.
        que = queue.Queue()
        count = 1
        if not root:
            return root
        que.put([root, count])
        count += 1

        while not que.empty():
            node, current = que.get()

            if (current & (current + 1) == 0):
                node.next = None
            else:
                node.next = que.queue[0][0]

            if not node.left:
                continue
            que.put([node.left, count])
            count += 1
            que.put([node.right, count])
            count += 1
        return root
