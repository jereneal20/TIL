class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        min_count = len(tops)

        for i in range(1, 7):
            count_t = 0
            count_b = 0
            for idx in range(len(tops)):
                if tops[idx] == i:
                    count_t += 1
                if bottoms[idx] == i:
                    count_b += 1

                if tops[idx] != i and bottoms[idx] != i:
                    count_t = -1
                    count_b = -1
                    break

            if count_t != -1:
                min_count = min(min_count, len(tops) - count_t, len(tops) - count_b)

        if min_count == len(tops):
            return -1
        return min_count