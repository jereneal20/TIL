class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        st = set()
        for num in nums:
            if num - k in mp:
                st.add((min(num - k, num), max(num - k, num)))
            if k + num in mp:
                st.add((min(k + num, num), max(k + num, num)))
            mp[num] += 1
        return len(st)


