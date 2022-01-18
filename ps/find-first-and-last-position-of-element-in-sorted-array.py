class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def recurse(left, right):
            mid = (left + right) // 2
            if nums[left] == target == nums[right]:
                return [left, right]
            if nums[left] <= target <= nums[right]:
                l, r = recurse(left, mid), recurse(mid + 1, right)
                if -1 in l:
                    return r
                if -1 in r:
                    return l
                return [l[0], r[1]]
            return [-1, -1]

        return recurse(0, len(nums) - 1)