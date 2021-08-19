class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        i, j = 0, len(s)

        for ch in s:
            if ch == 'I':
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
        res.append(i)
        return res