class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        # collections.Counter(s)
        sets = {}
        for char in s:
            if char in sets:
                sets[char] += 1
            else:
                sets[char] = 1
        count = 0
        # count = sum( val & 1 for val in sets.values())
        for val in sets.values():
            if val % 2 == 1:
                count += 1
        return count <= k and k <= len(s)
