class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i, j = 2, 2

        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i - 2]:
                j += 1
            if j == len(nums):
                break

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

        return i


