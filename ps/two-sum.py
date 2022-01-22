from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, num in enumerate(nums):
            if num in mp:
                return [idx, mp[num]]
            if target - num not in mp:
                mp[target - num] = idx
        return [-1, -1]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, e in enumerate(nums):
            m = target - e
            if m in dictionary:
                return [dictionary[m], i]
            dictionary[e] = i
        raise Exception()

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            raise Exception()

        numsWithIdxs = sorted((e, i) for i, e in enumerate(nums))
        i, j = 0, len(nums) - 1
        while i < j:
            if numsWithIdxs[i][0] + numsWithIdxs[j][0] < target:
                i += 1
            elif numsWithIdxs[i][0] + numsWithIdxs[j][0] > target:
                j -= 1
            else:
                return [numsWithIdxs[i][1], numsWithIdxs[j][1]]
        raise Exception()