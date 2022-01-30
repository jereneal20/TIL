class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))

        n = len(nums)
        l, r = pivot, pivot + n - 1
        while l % n != r % n:
            mid = (l + r) // 2
            if target == nums[mid % n]:
                return mid % n
            if target < nums[mid % n]:
                r = mid
            else:
                l = mid + 1

        if nums[l % n] == target:
            return l % n
        return -1

    # 4
    # 4, 10
    # 7 => 0 // 4
    # 4, 7
    # 5 => 5 // 1
    # 4, 5
    # 4 => 4 // 0 match

    # 1
    # 1 2
    # 1 => 1 // 1
    # 2 2

