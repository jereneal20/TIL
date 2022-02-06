class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def recurse(step, start, cur_set):
            if step == k:
                res.append(cur_set)
                return

            for i in range(start, n + 1):
                recurse(step + 1, i + 1, cur_set + [i])

        recurse(0, 1, [])
        return res