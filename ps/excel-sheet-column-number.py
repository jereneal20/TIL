class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for ch in columnTitle:
            num *= 26
            num += ord(ch) - ord('A') + 1
        return num