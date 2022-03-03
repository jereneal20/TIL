"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        deq = deque()
        copied = Node(node.val)
        mp = {node.val: copied}
        deq.append(node)
        while deq:
            node = deq.popleft()

            for neighbor in node.neighbors:
                if neighbor.val not in mp:

                    copy_neigh = Node(neighbor.val)
                    mp[neighbor.val] = copy_neigh
                    mp[node.val].neighbors.append(copy_neigh)

                    deq.append(neighbor)
                else:
                    mp[node.val].neighbors.append(mp[neighbor.val])

        return copied