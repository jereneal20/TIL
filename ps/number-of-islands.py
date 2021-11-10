class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue

                self.recursion(grid, i, j)
                count += 1
        return count

    def recursion(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == "0":
            return 0

        grid[i][j] = "0"

        count = 1
        # count += self.recursion(grid, i-1, j-1)
        count += self.recursion(grid, i, j - 1)
        # count += self.recursion(grid, i+1, j-1)
        count += self.recursion(grid, i - 1, j)
        count += self.recursion(grid, i + 1, j)
        # count += self.recursion(grid, i-1, j+1)
        count += self.recursion(grid, i, j + 1)
        # count += self.recursion(grid, i+1, j+1)

        return count