class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        mp = defaultdict(int)
        for val in arr:
            mp[val] += 1
        for val in target:
            mp[val] -= 1
        for key in mp:
            if mp[key] != 0:
                return False
        return True