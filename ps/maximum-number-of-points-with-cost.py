class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pre = [elem for elem in points[0]]
        lefts = [0] * len(points[0])
        rights = [0] * len(points[0])
        for i in range(1, len(points)):
            for j in range(len(points[0])):
                if j == 0:
                    lefts[j] = pre[j]
                else:
                    lefts[j] = max(pre[j], lefts[j-1]-1)

            for j in range(len(points[0]) - 1, -1, -1):
                if j == len(points[0]) - 1:
                    rights[j] = pre[j]
                else:
                    rights[j] = max(pre[j], rights[j+1]-1)

            for j in range(len(points[0])):
                pre[j] = max(lefts[j], rights[j]) + points[i][j]

        return max(pre)