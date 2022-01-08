class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.bfs(s, [], res)
        return res

    def bfs(self, s, palindromes, res):
        if not s:
            res.append(palindromes)

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.bfs(s[i:], palindromes + [s[:i]], res)

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]