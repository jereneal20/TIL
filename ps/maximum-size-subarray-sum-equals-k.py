class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mp = {0: -1}  # 1:0 5:2 3:3 6:4
        sum_so_far = 0
        max_length = 0
        for idx, num in enumerate(nums):
            sum_so_far += num
            if sum_so_far - k in mp:
                max_length = max(max_length, idx - mp[sum_so_far - k])

            if sum_so_far not in mp:
                mp[sum_so_far] = idx
        return max_length