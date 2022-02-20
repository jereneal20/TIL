class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def combination(nums, i):
            result = []

            def recurse(nums, depth, idx, res):
                # print(res)
                # if depth == idx:
                result.append(res)
                for i, _ in enumerate(nums):
                    recurse(nums[i + 1:], depth + 1, idx, res + [nums[i]])

            recurse(nums, 0, i, [])
            return result

        return combination(nums, 2)

        # for i in range(len(nums)+1):
        #     res += map(list, combinations(nums, i))
        # return res