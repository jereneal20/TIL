class Solution:
    def rob(self, nums: List[int]) -> int:
        # Do it for 0~n-2 and 1~n-1, and get one of them
        if len(nums) < 3:
            return max(nums)
        max_rob = [0] * (len(nums)+2)
        max_val = 0
        for i in range(len(nums)-1):
            max_rob[i] = max(max_rob[i-1], max_rob[i-2]+nums[i])
        max_val = max_rob[len(nums)-2]
        max_rob = [0] * (len(nums)+2)
        for i in range(1, len(nums)):
            max_rob[i] = max(max_rob[i-1], max_rob[i-2]+nums[i])
        return max(max_val, max_rob[len(nums)-1])