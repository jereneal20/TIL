# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:
            if cur1:
                cur1 = cur1.next
            else:
                cur1 = headB
            if cur2:
                cur2 = cur2.next
            else:
                cur2 = headA

        return cur1
		
