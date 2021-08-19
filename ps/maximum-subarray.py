class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            nums[i] = max(nums[i - 1] + num, num)
            res = max(res, nums[i])

        return res