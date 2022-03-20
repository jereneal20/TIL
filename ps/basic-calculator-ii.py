class Solution:
    def calculate(self, s: str) -> int:
        stk = []

        def update_stk(num, sig):
            if sig == '+':
                stk.append(num)
            if sig == '-':
                stk.append(-num)
            if sig == '*':
                stk.append(stk.pop() * num)
            if sig == '/':
                stk.append(int(stk.pop() / num))

        i, num = 0, 0
        sign = '+'
        while i < len(s):
            if s[i].isnumeric():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/":
                update_stk(num, sign)
                num, sign = 0, s[i]
            i += 1

        update_stk(num, sign)
        return sum(stk)