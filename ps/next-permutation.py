class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) - 1, len(nums) - 1

        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1

        if i == 0:
            nums.reverse()
            return
        k = i - 1

        while j > k:
            if nums[k] < nums[j]:
                nums[k], nums[j] = nums[j], nums[k]
                break
            j -= 1

        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return
