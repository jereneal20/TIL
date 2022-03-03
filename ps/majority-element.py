class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        for num in mp:
            if mp[num] > len(nums)//2:
                return num