class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for digit in num:
            while k > 0 and len(stk) > 0 and digit < stk[-1]:
                stk.pop()
                k -= 1
            stk.append(digit)
        if k > 0:
            stk = stk[:-k]
        return "".join(stk).lstrip("0") or "0"
