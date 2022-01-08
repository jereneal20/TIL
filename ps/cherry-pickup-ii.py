class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 로봇이 하나라면 DP 테이블 하나만 있으면 되는데, 두개라 그 두개에 대한 각각의 maximum을 dp 테이블로 저장해야되서 2차원 dp 테이블을 써야하는 것.
        # 이외에는 로봇이 하나라 생각하고 초반에 로봇이 갈 수 있는 부분 제한하는 조건 설정하는 것 빼면 기존 DP랑 다름없다.
        col_num = len(grid[0])
        dp = [[0] * col_num for i in range(col_num)]

        dp[0][col_num - 1] = grid[0][0] + grid[0][col_num - 1]

        for row_idx in range(1, len(grid)):
            cur_dp = [[0] * col_num for i in range(col_num)]
            for i in range(min(col_num, row_idx + 1)):
                for j in range(col_num - 1, max(-1, col_num - 1 - row_idx - 1), -1):
                    max_val = 0
                    # print(dp)
                    for i1 in [-1, 0, 1]:
                        for j1 in [-1, 0, 1]:
                            if (0 <= i + i1 < col_num) and (0 <= j + j1 < col_num):
                                max_val = max(max_val, dp[i + i1][j + j1])
                    if i == j:
                        cur_dp[i][j] = max_val + grid[row_idx][i]
                    else:
                        cur_dp[i][j] = max_val + grid[row_idx][i] + grid[row_idx][j]
            dp = cur_dp
        max_val = 0
        for i in range(col_num):
            for j in range(col_num):
                max_val = max(max_val, dp[i][j])
        return max_val
