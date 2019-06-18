# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class CBTInserter:
    clist = list()
    def __init__(self, root: TreeNode):
        self.clist = list()
        que = queue.Queue()
        self.clist.append(None)
        que.put(root)
        while que.qsize() != 0:
            cur = que.get()
            if not cur:
                break
            self.clist.append(cur)
            que.put(cur.left)
            que.put(cur.right)

    def insert(self, v: int) -> int:
        node = TreeNode(v)

        parent_idx = len(self.clist)//2
        parent_node = self.clist[parent_idx]
        
        if len(self.clist) % 2 != 0:
	        parent_node.right = node
        else:
            parent_node.left = node
        self.clist.append(node)
        return parent_node.val

    def get_root(self) -> TreeNode:
        if len(self.clist) <= 1:
            return None
        return self.clist[1]
    

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
