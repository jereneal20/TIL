class Solution:
    def numberOfSteps(self, num: int) -> int:
        return bin(num).count("1") * 2 + bin(num).count("0") - 1 - 1
    # 0b1010

    # count = 0
    # while num != 0:
    #     if num % 2 == 0:
    #         num /= 2
    #     else:
    #         num -= 1
    #     count += 1
    # return count