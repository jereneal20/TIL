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
