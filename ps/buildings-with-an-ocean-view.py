class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        height_so_far = 0
        res = []
        for idx, height in enumerate(heights[::-1]):
            idx = len(heights) - 1 - idx
            if height > height_so_far:
                res.append(idx)
                height_so_far = height

        return res[::-1]