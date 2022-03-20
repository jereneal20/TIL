# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        count = 0
        node = head
        last = None
        while node:
            count += 1
            if not node.next:
                last = node
            node = node.next

        k = count - k % count
        if k == 0:
            return head

        last.next = head
        node = head
        while k > 0:
            last = node
            node = node.next
            k -= 1
        last.next = None

        return node