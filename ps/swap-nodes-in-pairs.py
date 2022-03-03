# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        node = dummy
        while node:
            if not node.next:
                break
            if not node.next.next:
                break
            first = node.next
            second = first.next

            first.next = second.next
            second.next = first
            node.next = second

            node = first
        return dummy.next