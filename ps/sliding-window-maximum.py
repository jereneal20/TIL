class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6
        deq = deque()
        res = []
        for idx, num in enumerate(nums):
            while len(deq) != 0 and nums[deq[-1]] < num:
                deq.pop()
            deq.append(idx)

            res.append(nums[deq[0]])
            while len(deq) != 0 and deq[0] <= idx - k + 1:
                deq.popleft()

        return res[k - 1:]