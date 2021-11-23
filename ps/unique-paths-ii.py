class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        arr = [[1]*m for i in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == 1:
                    arr[i][j] = 0
                else:
                    if i == 0:
                        arr[i][j] = arr[i][j-1]
                    elif j == 0:
                        arr[i][j] = arr[i-1][j]
                    else:
                        arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[n-1][m-1]