class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        last = intervals[0]
        for interval in intervals[1:]:
            if last[1] <= interval[0]:
                last = interval
            else:
                count += 1
        return count
