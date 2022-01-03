class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        has_truster = {}
        has_trustee = {}
        for trustee, truster in trust:
            if trustee not in has_truster:
                has_truster[trustee] = []
            has_truster[trustee].append(truster)

            if truster not in has_trustee:
                has_trustee[truster] = []
            has_trustee[truster].append(trustee)
        # print(has_truster)
        # print(has_trustee)
        for i in range(1, n + 1):
            if i not in has_trustee:
                continue
            if len(has_trustee[i]) == n - 1 and i not in has_truster:
                return i
        return -1
