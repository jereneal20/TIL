class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mp = defaultdict(int)
        for num in nums:
            mp[num] += num

        mp_list = list(sorted(mp))

        dp = [0] * (mp_list[-1] + 1)
        res = 0
        for num in range(mp_list[-1] + 1):
            if num == 0 or num == 1:
                dp[num] = mp[num]
                continue
            dp[num] = max(dp[num - 1], mp[num] + dp[num - 2])
            res = max(res, dp[num])
        return res
