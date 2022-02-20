class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        arr = nums
        if len(arr) == 3:
            return arr[0] * arr[1] * arr[2]

        heap = []
        heap2 = []

        for val in arr:
            if len(heap) < 3:
                heapq.heappush(heap, val)
            elif heap[0] < val:
                heapq.heappop(heap)
                heapq.heappush(heap, val)

            if len(heap2) < 2:
                heapq.heappush(heap2, -val)
            elif heap2[0] < -val:
                heapq.heappop(heap2)
                heapq.heappush(heap2, -val)
        #         print(heap)
        #         print(heap2)

        val = max(heap)
        return max(heap[0] * heap[1] * heap[2], val * heap2[0] * heap2[1])