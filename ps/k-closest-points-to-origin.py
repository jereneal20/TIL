def euc_dist(point: List[int]):
    return point[0] ** 2 + point[1] ** 2


class Solution:
    # Try it againt with the best solution.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l, r, pivot = 0, len(points) - 1, len(points)
        while k != pivot:
            pivot = self.partition(points, l, r)
            print(pivot)
            if k < pivot:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:pivot]

    def partition(self, points, l, r):
        pivot = (l + r) // 2
        j = l
        points[pivot], points[r] = points[r], points[pivot]
        pivot_dist = euc_dist(points[r])
        for i in range(l, r + 1):
            if euc_dist(points[i]) <= pivot_dist:
                points[i], points[j] = points[j], points[i]
                j += 1
        return j - 1

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:k]