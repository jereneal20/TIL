# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random


class Solution:
    # reservoir sampling
    # https://trancekim.tistory.com/3#:~:text=Reservoir%20Sampling%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%80%20i,%EA%B0%92)%EC%9D%84%20%EC%9C%A0%EC%A7%80%ED%95%98%EB%9D%BC%EA%B3%A0%20%EB%A7%90%ED%95%A9%EB%8B%88%EB%8B%A4.
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        i = 1
        cur = self.head
        selected = cur
        while cur != None:
            if random.random() < (1 / i):
                selected = cur
            i += 1
            cur = cur.next
        return selected.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()