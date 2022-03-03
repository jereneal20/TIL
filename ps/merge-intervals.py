class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        for interval in intervals:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                res.append(prev)
                prev = interval
        res.append(prev)
        return res