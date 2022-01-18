class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        deq = deque()
        deq.append(0)

        idx = minJump
        while len(deq) != 0 and idx < len(s):
            zero = deq.popleft()
            while idx < len(s) and idx <= zero + maxJump:
                if s[idx] == '0' and zero + minJump <= idx:
                    deq.append(idx)
                idx += 1

        if len(deq) == 0 or deq[-1] != len(s) - 1:
            return False
        return True

#         for idx, ch in enumerate(s):
#             if idx == 0 or ch == '1':
#                 continue

#             while len(deq) != 0 and not (idx - maxJump <= deq[-1]):
#                 deq.popleft()
#                 print(deq)

#             if len(deq) != 0 and idx - maxJump <= deq[-1] <= idx - minJump:
#                 deq.append(idx)
#                 print(deq)

#         if len(deq) == 0 or deq[-1] != len(s) - 1:
#             return False
#         return True


