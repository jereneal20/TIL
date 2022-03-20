class Solution:
    def countOrders(self, n: int) -> int:
        i = 2
        res = 1

        while i <= n:
            res *= ((i * 2) * (i * 2 - 1)) // 2
            res %= 1000000007
            i += 1

        return res

