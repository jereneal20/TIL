class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_val = sys.maxsize
        for idx, val in enumerate(nums):
            i = idx + 1
            j = len(nums) - 1
            while i < j:
                candid = (nums[i] + nums[j] + val)
                diff = target - candid
                if abs(diff) < abs(min_val):
                    min_val = diff
                if diff > 0:
                    i += 1
                elif diff < 0:
                    j -= 1
                else:
                    return target

        return target - min_val
        
