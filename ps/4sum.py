class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        seen = set()
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        res.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return res

    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        mp = defaultdict(list)
        res = {}
        for i in range(n):
            for j in range(i + 1, n):
                mp[nums[i] + nums[j]].append([i, j])

        for i in range(n):
            for j in range(i + 1, n):
                if target - (nums[i] + nums[j]) in mp:
                    for a, b in mp[target - (nums[i] + nums[j])]:
                        if a in [i, j] or b in [i, j]:
                            continue
                        if tuple(sorted([nums[i], nums[j], nums[a], nums[b]])) not in res:
                            res[tuple(sorted([nums[i], nums[j], nums[a], nums[b]]))] = 1

        return map(list, res.keys())