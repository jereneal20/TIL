class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []

        for val in nums:
            if val % 2 != 0:
                val *= 2
            heappush(heap, -val)
        # all values are even now.

        min_val = -max(heap)
        max_val = -heap[0]
        min_deviation = max_val - min_val

        while (-heap[0]) % 2 == 0:
            val = -heappop(heap)
            max_val = max(val // 2, -heap[0])
            if val // 2 < min_val:
                min_val = val // 2
            # print(min_val)
            # print(max_val)
            # print(min_deviation)
            if min_deviation > max_val - min_val:
                min_deviation = max_val - min_val

            heappush(heap, -(val // 2))
        # print(heap)
        return min_deviation


