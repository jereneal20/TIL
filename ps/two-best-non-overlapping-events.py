import heapq


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events.sort(key=lambda event: event[0])
        heap = []
        maxSum = 0
        left_max_so_far = 0
        for event in events:
            start, end, value = event
            while heap and heap[0][1][1] < start:
                elem = heapq.heappop(heap)
                # 어떤 n 번째 node에 대해 최대 합은 그 node의 시작점에서 이미 끝난 node 중 최대값과 현재 node를 더하는 것.
                # 최대 2개만 가질 수 있기 때문에 가능.
                left_max_so_far = max(left_max_so_far, elem[1][2])
                # maxSum과 이 값을 따로 하는 이유는, 이 값은 다음 event에서도 최대 값으로서 활용할 수 있기 때문. (start는 점점 커지기 때문에 이 값이 invalid해 질 일은 없다.)

            maxSum = max(maxSum, left_max_so_far + value)
            heapq.heappush(heap, (end, event))

        while heap:
            elem = heapq.heappop(heap)
            maxSum = max(maxSum, elem[1][2])

        return maxSum