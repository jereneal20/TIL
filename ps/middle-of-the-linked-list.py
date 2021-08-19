# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeI = head
        nodeJ = head
        while nodeJ != None:
            nodeJ = nodeJ.next
            if nodeJ == None:
                return nodeI
            nodeI = nodeI.next
            nodeJ = nodeJ.next
        return nodeI


