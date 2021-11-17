class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        start = 0
        end = len(mat) - 1
        while start <= end:
            mid = (int)((start + end) / 2)
            idx = self.findMaxIdx(mat[mid])
            way = self.isPeak(mat, mid, idx)
            if way == 0:
                return [mid, idx]
            if way == 1:
                start = mid + 1
            else:
                end = mid - 1

    def findMaxIdx(self, nums):
        return nums.index(max(nums))

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

    def isPeak(self, nums, i, idx):
        if i == 0 and i == len(nums) - 1:
            return 0
        if i == 0 and nums[i][idx] < nums[i + 1][idx]:
            return 1
        if i == len(nums) - 1 and nums[i][idx] < nums[i - 1][idx]:
            return -1
        if i == 0 or i == len(nums) - 1:
            return 0

        if nums[i][idx] < nums[i + 1][idx]:
            return 1
        if nums[i][idx] < nums[i - 1][idx]:
            return -1
        if nums[i][idx] > nums[i + 1][idx] and nums[i][idx] > nums[i - 1][idx]:
            return 0
        return 1