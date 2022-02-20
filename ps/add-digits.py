class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            cur = num
            res = 0
            while cur != 0:
                res += cur % 10
                cur //= 10
            num = res
        return num