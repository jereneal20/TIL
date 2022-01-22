class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l < r:
            # print(str(l) + " " + str(r))
            k = (l + r) // 2
            if self.eatableInHours(piles, h, k):
                r = k
            else:
                l = k + 1
        return l

    def eatableInHours(self, piles, h, k):
        count = 0
        for pile in piles:
            count += pile // k
            count += 1 if pile % k != 0 else 0
        return count <= h