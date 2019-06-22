class Solution:
    def trap(self, height: List[int]) -> int:
        water_sum = 0
        stk = []
        for idx, cur in enumerate(height):
            while len(stk) != 0 and height[stk[-1]] <= cur:
                if len(stk) > 1:
                    water_sum += (min(height[stk[-2]], cur) - height[stk[-1]]) * (idx - stk[-2] - 1)
                del stk[-1]
            
            if len(stk) == 0 or height[stk[-1]] > cur:
                stk.append(idx)
        return water_sum
