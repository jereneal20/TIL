class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = 1
        while n > res:
            res = res * 2 + 1
        return (n ^ res)