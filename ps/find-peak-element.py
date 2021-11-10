class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (int)((start + end) / 2)
            way = self.isPeak(nums, mid)
            if way == 0:
                return mid
            if way == 1:
                start = mid + 1
            else:
                end = mid - 1

    def isPeak(self, nums, i):
        if i == 0 and i == len(nums) - 1:
            return 0
        if i == 0 and nums[i] < nums[i + 1]:
            return 1
        if i == len(nums) - 1 and nums[i] < nums[i - 1]:
            return -1
        if i == 0 or i == len(nums) - 1:
            return 0

        if nums[i] < nums[i + 1]:
            return 1
        if nums[i] < nums[i - 1]:
            return -1
        if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            return 0
        return 1