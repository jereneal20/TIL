import queue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        que = queue.Queue()
        if len(lists) == 0:
            return None

        for lis in lists:
            que.put(lis)

        while que.qsize() > 1:
            que.put(self.mergeTwoLists(que.get(), que.get()))
            print(que.qsize())
        return que.get()

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        point = res
        while l1 and l2:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next

        while l1:
            point.next = l1
            l1 = l1.next
            point = point.next
        while l2:
            point.next = l2
            l2 = l2.next
            point = point.next

        return res.next