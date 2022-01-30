class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        sqs = [1]
        i = 2
        while i * i <= n:
            sqs.append(i * i)
            i += 1

        for i in range(1, n + 1):
            if dp[i] != 0:
                continue

            j = 0
            while j < len(sqs) and sqs[j] <= i:
                if dp[i - sqs[j]] % 2 == 0:
                    dp[i] = dp[i - sqs[j]] + 1
                    break
                j += 1
            if dp[i] == 0:
                dp[i] = dp[i - 1] + 1

            if dp[i] % 2 == 0:
                self.fillCases(dp, sqs, i)

        # print(sqs)
        # print(dp)
        return dp[n] % 2 != 0

    def fillCases(self, dp, sqs, i):
        # losing case (even) + 1 is winning case
        for sq in sqs:
            if i + sq >= len(dp):
                return
            dp[i + sq] = dp[i] + 1

            # 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> x => #5 -> should go to the odd #number if possible
            # 5 -> 1 -> 0 -> x => #2

