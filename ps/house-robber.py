class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev_norob = 0
        prev_rob = nums[0]
        for num in nums[1:]:
            rob = max(prev_rob, prev_norob + num)
            norob = max(prev_rob, prev_norob)
            prev_norob = norob
            prev_rob = rob
        return max(rob, norob)
