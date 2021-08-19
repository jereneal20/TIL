class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_num = max(len(num1), len(num2))
        reversed_num1 = num1[::-1]
        reversed_num2 = num2[::-1]

        carry = False
        res = ''
        for idx in range(max_num):
            if len(reversed_num1) <= idx:
                reversed_num1 += '0'
            if len(reversed_num2) <= idx:
                reversed_num2 += '0'

            added_num = int(reversed_num1[idx]) + int(reversed_num2[idx]) # use ord('0') later.
            if carry:
                added_num += 1
                carry = False

            if added_num >= 10:
                added_num -= 10
                carry = True
            res += str(added_num)

        if carry:
            res += '1'

        return res[::-1]