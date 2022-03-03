from functools import cmp_to_key


def comp(intervalA, intervalB):
    if intervalA[0] != intervalB[0]:
        return intervalA[0] > intervalB[0]
    return intervalA[1] < intervalB[1]


def keyf(interval):
    return (interval[0], -interval[1])


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=keyf)
        mp = {}
        last = intervals[0]
        count = 0
        # print(intervals)
        for interval in intervals[1:]:
            if interval[1] <= last[1]:
                count += 1
            else:
                last = interval

        return len(intervals) - count