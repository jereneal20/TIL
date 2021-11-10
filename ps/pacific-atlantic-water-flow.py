class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_flowable = [[False] * len(heights[0]) for i in range(len(heights))]
        atl_flowable = [[False] * len(heights[0]) for i in range(len(heights))]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    self.recursion2(heights, pac_flowable, i, j, heights[i][j])
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    self.recursion2(heights, atl_flowable, i, j, heights[i][j])

        ret = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pac_flowable[i][j] and atl_flowable[i][j]:
                    ret.append([i, j])
        return ret

    def recursion2(self, heights, flowable, i, j, prev_height):
        if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]):
            return
        if flowable[i][j]:  # already visited
            return
        if heights[i][j] < prev_height:
            return

        flowable[i][j] = True
        self.recursion2(heights, flowable, i, j - 1, heights[i][j])
        self.recursion2(heights, flowable, i - 1, j, heights[i][j])
        self.recursion2(heights, flowable, i, j + 1, heights[i][j])
        self.recursion2(heights, flowable, i + 1, j, heights[i][j])
