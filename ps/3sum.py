class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        idx = 0
        while idx < len(nums):
            i = idx + 1
            j = len(nums) - 1
            while i < j:
                if -nums[idx] == nums[i] + nums[j]:
                    res.append([nums[idx], nums[i], nums[j]])

                    curi = nums[i]
                    while i < j and curi == nums[i]:
                        i += 1
                    curj = nums[j]
                    while i < j and curj == nums[j]:
                        j -= 1

                elif -nums[idx] < nums[i] + nums[j]:
                    j -= 1
                else:
                    i += 1

            cur = nums[idx]
            while idx < len(nums) and cur == nums[idx]:
                idx += 1

        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = []
        for idx, num in enumerate(nums):
            mp = {}
            for i in range(idx + 1, len(nums)):
                if -(num + nums[i]) in mp:
                    res.append(sorted([num, nums[i], mp[-(num + nums[i])]]))
                mp[nums[i]] = nums[i]
        res.sort()
        res2 = []
        [res2.append(x) for x in res if x not in res2]
        return res2


#     1 2 -3

#     a + b = -c

#   b = -a -c
#   c = -a - b

class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = list()
        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue
            i = idx + 1
            j = len(nums) - 1
            while i < j:
                target = val + nums[i] + nums[j]
                # print([val, nums[i], nums[j]])
                if target == 0:
                    res.append([val, nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    
                elif target < 0:
                    i += 1
                else:
                    j -= 1
        return res
