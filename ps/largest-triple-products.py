import math
import heapq


def findMaxProduct(arr):
    if len(arr) < 3:
        return [-1] * len(arr)
    if len(arr) == 3:
        return [-1, -1, arr[0] * arr[1] * arr[2]]

    heap = []
    heapq.heappush(heap, arr[0])
    heapq.heappush(heap, arr[1])
    heapq.heappush(heap, arr[2])
    res = [-1, -1, heap[0] * heap[1] * heap[2]]
    for val in arr[3:]:
        if heap[0] < val:
            heapq.heappop(heap)
            heapq.heappush(heap, val)

        res.append(heap[0] * heap[1] * heap[2])

    return res

#
# arr_1 = [1, 2, 3, 4, 5]
# expected_1 = [-1, -1, 6, 24, 60]
# output_1 = findMaxProduct(arr_1)
# check(expected_1, output_1)
#
# arr_2 = [2, 4, 7, 1, 5, 3]
# expected_2 = [-1, -1, 56, 56, 140, 140]