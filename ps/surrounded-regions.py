class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" or board[i][j] == "A":
                    continue

                ret = self.recursion(board, i, j)
                if not ret:
                    self.make_x_region(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "A":
                    board[i][j] = "O"

    def make_x_region(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == "X":
            return

        grid[i][j] = "X"

        self.make_x_region(grid, i, j - 1)
        self.make_x_region(grid, i - 1, j)
        self.make_x_region(grid, i + 1, j)
        self.make_x_region(grid, i, j + 1)

        return

    def recursion(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return True
        if grid[i][j] == "A":
            return False
        if grid[i][j] == "X":
            return False

        grid[i][j] = "A"

        ret = False
        ret |= self.recursion(grid, i, j - 1)
        ret |= self.recursion(grid, i - 1, j)
        ret |= self.recursion(grid, i + 1, j)
        ret |= self.recursion(grid, i, j + 1)

        return ret