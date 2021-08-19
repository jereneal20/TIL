class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            num_of_one = 0
            for num in nums:
                if (pow(2, i) & num) > 0:
                    num_of_one += 1
            res += num_of_one * (len(nums) - num_of_one)
        return res

    def totalHammingDistance2(self, nums: List[int]) -> int:
        res = 0
        bin_nums = []
        for num in nums:
            bin_nums.append(bin(num))
        for i in range(0, -32, -1):
            num_of_one = 0
            for j in range(len(bin_nums)):
                if len(bin_nums[j]) > -i + 2:
                    num_of_one += int(bin_nums[j][i - 1])
            res += num_of_one * (len(bin_nums) - num_of_one)

        return res