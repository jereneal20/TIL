class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        max_so_far = 0
        i = 0
        for j in range(1, len(values)):
            # 최선의 left node index를 항상 업데이트해나간다. 이전까지의 최고와 현재 index를 비교해서 더 크다면 (-1포함), 예전걸 그대로 쓰면되고, 아니면 새로운걸 쓰면된다. 이후 score를 구하고 그 score들 중 최고 값을 리턴.
            if values[i] + (i - (j - 1)) < values[j - 1]:
                i = j - 1

            max_so_far = max(max_so_far, values[i] + values[j] + (i - j))

        return max_so_far