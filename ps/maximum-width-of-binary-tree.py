# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mp = defaultdict(list)

        def recurse(node, depth, width):
            if not node:
                return

            mp[depth].append(width)

            recurse(node.left, depth + 1, width * 2)
            recurse(node.right, depth + 1, width * 2 + 1)

        recurse(root, 0, 1)

        max_width = 0
        # print (mp)
        for key in mp:
            widths = mp[key]

            # widths.sort()
            max_width = max(max_width, widths[-1] - widths[0] + 1)
        return max_width