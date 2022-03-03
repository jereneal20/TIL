# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Think about the O(1) space complexity solution
        node = head
        li = []
        while node:
            li.append([node.val, node])
            node = node.next

        li.sort(key=lambda x: x[0])
        new_head = ListNode(-1)
        node = new_head
        for nd in li:
            node.next = nd[1]
            node = node.next
        node.next = None

        return new_head.next