class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.recurse(nums, [], res)
        return res

    def recurse(self, nums, cur_path, res):
        if not nums:
            res.append(cur_path)

        for i, num in enumerate(nums):
            self.recurse(nums[:i] + nums[i + 1:], cur_path + [num], res)

    def permute3(self, nums: List[int], k) -> List[List[int]]:
        res = []
        def recurse(nums, cur_path, res):
            if len(cur_path) == k:
                res.append(cur_path)
                return

            for i, num in enumerate(nums):
                recurse(nums[:i]+nums[i+1:], cur_path+[num], res)
        recurse(nums, [], res)
        return res