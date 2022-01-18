class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        left_stack, right_stack = [k], [k]
        self.left_end, self.right_end = -1, len(heights)

        def left_calculate(start):
            for idx in range(start - 1, -1, -1):
                if heights[idx + 1] > heights[idx]:
                    left_stack.append(idx)
                elif heights[idx + 1] < heights[idx]:
                    self.left_end = idx + 1
                    return
            self.left_end = 0

        def right_calculate(start):
            for idx in range(start + 1, len(heights)):
                if heights[idx - 1] > heights[idx]:
                    right_stack.append(idx)
                elif heights[idx - 1] < heights[idx]:
                    self.right_end = idx - 1
                    return
            self.right_end = len(heights) - 1

        left_calculate(k)
        right_calculate(k)

        for _ in range(volume):
            if left_stack[-1] != k:
                heights[left_stack[-1]] += 1

                if heights[left_stack[-1]] < heights[left_stack[-1] + 1]:
                    left_stack.append(left_stack[-1])

                if self.left_end == left_stack[-1]:
                    left_stack.pop()
                    left_calculate(self.left_end)
                else:
                    left_stack[-1] -= 1

            elif right_stack[-1] != k:
                heights[right_stack[-1]] += 1

                if heights[right_stack[-1]] != heights[right_stack[-1] - 1]:
                    right_stack.append(right_stack[-1])

                if self.right_end == right_stack[-1]:
                    right_stack.pop()
                    right_calculate(self.right_end)
                else:
                    right_stack[-1] += 1
            else:
                heights[left_stack[-1]] += 1
                left_calculate(k)
                right_calculate(k)

        return heights
