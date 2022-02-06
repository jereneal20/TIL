class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        mp = defaultdict(int)
        for i in nums3:
            for j in nums4:
                mp[i + j] += 1

        for i in nums1:
            for j in nums2:
                if -(i + j) in mp:
                    count += mp[-(i + j)]
        return count