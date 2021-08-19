class Solution:
    dialDict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
    res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.res = []
        self.enumerates(digits, 0, "")
        return self.res

    def enumerates(self, digits, index, combs):
        if index == len(digits):
            self.res.append(combs)
            return
        digit = digits[index]
        for char in self.dialDict[digit]:
            self.enumerates(digits, index + 1, combs + char)