class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        prev = points[0]
        count = 1
        for point in points[1:]:
            if prev[1] < point[0]:
                prev = point
                count += 1
            else:
                pass
        return count