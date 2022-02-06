class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(nums, 0, n - k % n - 1)
        reverse(nums, n - k % n, n - 1)
        nums.reverse()

        # n = len(nums)
        # nums2 = nums[n-(k)%n:] + nums[0:n-k%n]
        # for i, num in enumerate(nums2):
        #     nums[i] = nums2[i]