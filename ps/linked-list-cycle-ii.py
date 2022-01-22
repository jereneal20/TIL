# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start to meeting point of 2 pointer is same as the length of cycle
        if not head or not head.next:
            return None

        fast = head.next
        slow = head
        while fast != None and fast != slow:
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            slow = slow.next

        if not fast:
            return None

        slow = slow.next
        begin = head

        while begin != slow:
            begin = begin.next
            slow = slow.next

        return begin