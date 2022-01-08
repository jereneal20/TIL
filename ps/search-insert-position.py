class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, 0, len(nums), target)

    def bin_search(self, nums, start, end, target):
        mid = (start + end) // 2
        if end <= start:
            return mid
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bin_search(nums, mid + 1, end, target)
        else:
            return self.bin_search(nums, start, mid, target)