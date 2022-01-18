class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        stk = [(height[0], 0)]
        count = 0

        for idx, length in enumerate(height):
            if stk[-1][0] < length:
                stk.append((length, idx))

        max_so_far = 0
        for idx, length in enumerate(height[::-1]):
            idx = len(height) - 1 - idx

            max_so_far = max(max_so_far, length)
            if stk[-1][1] == idx:
                stk.pop()
                continue

            # if max_so_far > stk[-1][0]:
            #     count += stk[-1][0] - length
            # else:
            #     count += max_so_far - length
            count += min(max_so_far, stk[-1][0]) - length

        return count

        # 0 1 3 7


class Solution2:
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
