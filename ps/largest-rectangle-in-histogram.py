class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 줄었다 다시 커지면서 옛날 인덱스를 써야되는케이스를 고민해보자
        # 2 1 2는 높이 1로 계산할 때 인덱서 -1 자리로 넓이 계산해야함.
        maximum = heights[0]
        stk = [(-1, 0)]
        for idx, height in enumerate(heights + [0]):
            while stk and stk[-1][1] > height:
                idx2, height2 = stk.pop()
                H = height2
                W = idx - stk[-1][0] - 1
                maximum = max(maximum, H * W)

            stk.append((idx, height))
        return maximum