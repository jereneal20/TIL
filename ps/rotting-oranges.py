import queue


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = queue.Queue()
        max_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.put([i, j, 0])

        while not que.empty():
            x, y, cnt = que.get()
            if cnt > max_count:
                max_count = cnt

            for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if x + i < 0 or x + i >= len(grid):
                    continue
                if y + j < 0 or y + j >= len(grid[0]):
                    continue

                if grid[x + i][y + j] == 1:
                    grid[x + i][y + j] = 2
                    que.put([x + i, y + j, cnt + 1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return max_count