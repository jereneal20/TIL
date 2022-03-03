class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        diff = []
        for idx, num in enumerate(nums[:-1]):
            diff.append(nums[idx] - nums[idx + 1])

        same_diff_leng = 1
        prev_diff = diff[0]
        res = 0
        # print(diff)
        for num in diff[1:]:
            if num == prev_diff:
                same_diff_leng += 1
            else:
                prev_diff = num
                res += ((same_diff_leng) * (same_diff_leng - 1)) // 2
                same_diff_leng = 1

        res += ((same_diff_leng) * (same_diff_leng - 1)) // 2

        return res

#                 1 2 3 4 5 6

#                 1
#                 2+1
#                 3+2+1
#                 4+3+2+1
