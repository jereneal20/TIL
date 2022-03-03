class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        check_point = 0
        while i < len(nums):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
                if check_point != i:
                    res.append(str(nums[check_point]) + "->" + str(nums[i]))
                else:
                    res.append(str(nums[check_point]))
                check_point = i + 1
            i += 1
        return res