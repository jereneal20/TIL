class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        penalty = 0
        for ch in s:
            if ch == '(':
                count += 1
            else:
                count -= 1

            if count < 0:
                penalty += 1
                count = 0

        return count + penalty