import sys


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Time complexity 분석
        mp = {}
        for point in points:
            if point[0] not in mp:
                mp[point[0]] = {}
            mp[point[0]][point[1]] = 1
        min_sq = sys.maxsize

        passedx = {}
        for x in sorted(mp):
            ys = sorted(mp[x])
            for i, y1 in enumerate(ys):
                for j in range(i + 1, len(ys)):
                    y2 = ys[j]
                    if (y1, y2) in passedx:
                        min_sq = min(min_sq, abs((x - passedx[(y1, y2)]) * (y2 - y1)))
                    passedx[
                        (y1, y2)] = x  # store last x since the previous ones are no longer helpful for minimum square

        if min_sq == sys.maxsize:
            return 0
        return min_sq

    def minAreaRect2(self, points: List[List[int]]) -> int:
        mp = {}
        for point in points:
            if point[0] not in mp:
                mp[point[0]] = {}
            mp[point[0]][point[1]] = 1
        min_sq = sys.maxsize

        for i, p1 in enumerate(points):
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue

                if p2[1] not in mp[p1[0]] or p1[1] not in mp[p2[0]]:
                    continue

                min_sq = min(min_sq, abs((p1[0] - p2[0]) * (p1[1] - p2[1])))

        if min_sq == sys.maxsize:
            return 0
        return min_sq