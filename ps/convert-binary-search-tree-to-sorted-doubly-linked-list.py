"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    prev = None
    head = None

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        self.recurse(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def recurse(self, node):
        if not node:
            return

        self.recurse(node.left)
        if not self.prev:
            self.head = node
        else:
            self.prev.right = node
            node.left = self.prev
        self.prev = node
        self.recurse(node.right)
