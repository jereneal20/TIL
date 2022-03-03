class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        @cache
        def recurse(total, i):
            if total == 0:
                return True
            if total < 0 or len(nums) == i:
                return False
            return recurse(total - nums[i], i + 1) or recurse(total, i + 1)

        if sum(nums) % 2 == 1:
            return False
        return recurse(sum(nums) // 2, 0)
