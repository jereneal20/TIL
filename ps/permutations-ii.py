class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def recurse(nums, cur_perm):
            if not nums:
                res.append(cur_perm)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                recurse(nums[:i] + nums[i + 1:], cur_perm + [nums[i]])

        recurse(nums, [])
        return res
