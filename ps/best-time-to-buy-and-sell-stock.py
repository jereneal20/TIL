class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGap = 0
        stack = []
        for price in prices:
            if not stack:
                stack.append(price)
                continue
            if stack[-1] < price:
                maxGap = max(maxGap, price - stack[-1])
            else:
                stack.pop()
                stack.append(price)

        return maxGap