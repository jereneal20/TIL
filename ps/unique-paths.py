import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1] * m for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        return arr[n - 1][m - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))