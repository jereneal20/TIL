class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # 0은 empty set으로서 하나의 조합이 항상 존재.
        for coin in coins:
            for am in range(1, amount + 1):
                if am - coin < 0:
                    continue
                dp[am] += dp[am - coin]
        return dp[amount]

#         0 1 2 3 4 5
#        1  1 1 1 1 1
#        2  1 2 2 3 3
#        5  1 2 2 3 4
#        s  1 2 3 5


#         1
#         1+1, 2
#         1+1+1, 1+2
