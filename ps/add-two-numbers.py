# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode()
        node = dummy_head
        while l1 and l2:

            new_node = ListNode((l1.val + l2.val + carry) % 10)
            if l1.val + l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            node.next = new_node
            node = node.next
            l1 = l1.next
            l2 = l2.next

        if not l1:
            l1 = l2
        while l1:
            new_node = ListNode((l1.val + carry) % 10)
            if l1.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            node.next = new_node
            node = node.next
            l1 = l1.next

        if carry == 1:
            node.next = ListNode(1)

        return dummy_head.next