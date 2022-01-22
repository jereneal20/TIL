class Solution:
    def validPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                if s[:i] + s[i + 1:] == (s[:i] + s[i + 1:])[::-1] or s[:j] + s[j + 1:] == (s[:j] + s[j + 1:])[::-1]:
                    return True
                else:
                    return False
            i += 1
            j -= 1

        return True