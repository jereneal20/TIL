class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # N^3 을 N^2 로 줄이기 위한 array 만들기.
        # 해당 N^2 로직을 hash map을 이용해서 N으로 만들기
        # 예외 케이스인 처음부터 well performing interval 케이스를 추가.
        # https://leetcode.com/problems/longest-well-performing-interval/discuss/1166155/Trying-to-be-the-simplest-O(n)-explanation-in-Python
        longest = 0
        current = 0

        ntv_map = {}
        for hour_idx in range(len(hours)):
            if hours[hour_idx] > 8:
                current += 1
            else:
                current -= 1

            if current > 0:
                longest = hour_idx + 1

            if current not in ntv_map:
                ntv_map[current] = hour_idx

            if current - 1 in ntv_map:
                longest = max(longest, hour_idx - ntv_map[current - 1])

        return longest