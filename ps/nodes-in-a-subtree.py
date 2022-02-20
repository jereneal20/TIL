import math

class Node:
    def __init__(self, data):
        self.val = data
        self.children = []

def count_of_nodes(root, queries, s):
    # find node
    def find_node(node, val):
        if not node:
            return None
        if node.val == val:
            return node
        for child in node.children:
            node = find_node(child, val)
            if node:
                return node
        return None

    # find char from the node to the end
    # @cache
    def count_nodes_having_chars(node, ch, s):
        res = 0
        if not node:
            return 0
        if s[node.val - 1] == ch:
            res += 1
        for child in node.children:
            res += count_nodes_having_chars(child, ch, s)
        return res

    res = []
    for query in queries:
        node = find_node(root, query[0])
        res.append(count_nodes_having_chars(node, query[1], s))
    return res
