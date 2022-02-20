class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def dfs(target, index, path):
            if index == len(candidates):
                return
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(target - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return res