class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        i, j = self.get_start_sq(grid)
        self.zero_sqs = self.get_zero_sq_num(grid)
        self.count = 0

        self.recurse(grid, i - 1, j, 1)
        self.recurse(grid, i, j - 1, 1)
        self.recurse(grid, i + 1, j, 1)
        self.recurse(grid, i, j + 1, 1)

        return self.count

    def recurse(self, grid, i, j, step):
        if i == -1 or j == -1 or i == len(grid) or j == len(grid[0]) or grid[i][j] == -1 or grid[i][j] == 1:
            return
        if grid[i][j] == 2:
            if self.zero_sqs + 1 == step:
                self.count += 1
            return

        grid[i][j] = 1

        self.recurse(grid, i - 1, j, step + 1)
        self.recurse(grid, i, j - 1, step + 1)
        self.recurse(grid, i + 1, j, step + 1)
        self.recurse(grid, i, j + 1, step + 1)

        grid[i][j] = 0

        return

    def get_start_sq(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return (i, j)

    def get_zero_sq_num(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    count += 1
        return count