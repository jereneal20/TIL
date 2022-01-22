class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        res = []
        for ch in s:
            if ch == '(':
                count += 1
            if ch == ')':
                if count == 0:
                    continue
                count -= 1
            res.append(ch)

        count = 0
        res2 = []
        for ch in res[::-1]:
            if ch == ')':
                count += 1
            if ch == '(':
                if count == 0:
                    continue
                count -= 1
            res2.append(ch)

        return "".join(res2[::-1])