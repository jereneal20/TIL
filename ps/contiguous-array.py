class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
        count = 0
        max_length = 0
        mp = {0: -1}
        for idx, num in enumerate(nums):
            if num == 0:
                count += 1
            else:
                count -= 1

            if count in mp:
                max_length = max(max_length, idx - mp[count])
            else:
                mp[count] = idx
        return max_length
