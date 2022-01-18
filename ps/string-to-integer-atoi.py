class Solution:
    def myAtoi(self, s: str) -> int:
        sign, i = 1, 0
        while i < len(s) and s[i] == " ": i += 1

        if i < len(s) and s[i] in ['-', '+']:
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            if num > 2 ** 31: num = 2 ** 31

        num *= sign
        if num == 2 ** 31: num -= 1

        return num
