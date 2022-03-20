class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stk = []
        while i < len(pushed):
            stk.append(pushed[i])
            i += 1
            while len(stk) != 0 and popped[j] == stk[-1]:
                stk.pop()
                j += 1

        if len(stk) != 0:
            return False
        return True