def change_to_str(nums):
    return "".join([str(v) for v in nums])


def func(nums):
    return int(change_to_str(nums))


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        nums = arr
        if len(nums) < 3:
            return [-1, -1]

        count = nums.count(1)
        if count == 0:
            return [0, len(nums) - 1]
        if count % 3 != 0:
            return [-1, -1]

        j = len(nums) - 1
        a_third_count = count // 3  # 2

        while j >= 0:
            if nums[j] == 1:
                a_third_count -= 1
            if a_third_count == 0:
                break
            j -= 1

        length_of_pattern = len(nums) - j
        start_of_first_pat = change_to_str(nums[:j]).find(change_to_str(nums[j:]))
        if start_of_first_pat == -1:
            return [-1, -1]

        start_of_second = start_of_first_pat + length_of_pattern

        start_of_second_pat = change_to_str(nums[:j]).find(change_to_str(nums[j:]), start_of_second)
        if start_of_second_pat == -1:
            return [-1, -1]

        return [start_of_second - 1, start_of_second_pat + length_of_pattern]