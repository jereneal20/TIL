# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-200)
        dummy_head.next = head

        prev = dummy_head
        node = prev.next
        while node:
            if not node.next:
                return dummy_head.next

            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy_head.next