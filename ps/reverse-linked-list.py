# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.head = ListNode(0)
        self.cur = self.head
        
        self.recurse(head)
        return self.head.next
    
    def recurse(self, curr):
        if not curr:
            return
        self.recurse(curr.next)
        self.cur.next = ListNode(curr.val)
        self.cur = self.cur.next
        
