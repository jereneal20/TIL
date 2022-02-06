class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in nums]
        # for i in range(len(nums) - 3, -1, -1):
        #     for j in range(i + 2, len(nums)):
        for gap in range(len(nums) - 2):
            gap += 2

            i = 0
            while i < len(nums) - gap:
                j = i + gap
                dp[i][j] = max([dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j] for k in range(i + 1, j)])
                # print(str(i) + " " + str(j))
                i += 1

                # 11 22 33 44
                # 12 23 34 45
                # 13 24 35
        # print(dp)
        return dp[0][len(nums) - 1]

#         nums = [1] + nums + [1]  # add the dummy head and tail, both are left till end and DO NOT burst them.
#         mem = collections.defaultdict(int)  # standard memory trick to avoid repeated function calculations

#         def search(nums):
#             # print(nums)
#             if tuple(nums) in mem:  # standard memory trick to avoid repeated function calculations
#                 return mem[tuple(nums)]
#             ans = [0] * len(nums)

#             for i in range(1, len(nums) - 1):
#                 ans[i] = search(nums[:i + 1]) + search(nums[i:]) + nums[0] * nums[i] * nums[-1]
#             # print(ans)
#             mem[tuple(nums)] = max(ans)
#             return mem[tuple(nums)]

#         return search(nums)

# 1 2 3 4 5
# 2 + 2*3 + 3*4 + 4*5 + 5
# 2*3*4 + 2*4*5 + 2*5 + 5 + 5