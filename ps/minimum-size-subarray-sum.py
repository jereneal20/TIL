class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        minimum_len = len(nums)
        sum_of_nums = 0
        i, j = 0, -1
        while i < len(nums):
            sum_of_nums += nums[i]
            while sum_of_nums >= target:
                minimum_len = min(minimum_len, i - j)

                j += 1
                sum_of_nums -= nums[j]
            i += 1
        return minimum_len


