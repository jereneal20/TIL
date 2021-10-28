class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = 0
        tiring_day = 0
        non_tiring_day = 0
        for hour in hours:
            if tiring_day == 0:
                if hour <= 8:
                    continue
            if hour > 8:
                tiring_day += 1
                continue

            non_tiring_day += 1
            if tiring_day <= non_tiring_day:
                res = max(res, tiring_day + non_tiring_day - 1)
                tiring_day = 0
                non_tiring_day = 0

        if tiring_day * 2 - 1 <= len(hours):
            res = max(res, tiring_day * 2 - 1)
        return max(res, tiring_day + non_tiring_day - 1)
