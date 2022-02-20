class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                stk.append(ch)
            else:
                if len(stk) == 0:
                    return False
                if (ch == '}' and stk[-1] == '{') or (ch == ')' and stk[-1] == '(') or (ch == ']' and stk[-1] == '['):
                    stk.pop()
                else:
                    return False
        if len(stk) != 0:
            return False
        return True
