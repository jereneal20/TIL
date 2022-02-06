class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp1 = {}
        mp2 = {}
        for ch in p:
            if ch not in mp1:
                mp1[ch] = 0
            mp1[ch] += 1

        for ch in s[:len(p)]:
            if ch not in mp2:
                mp2[ch] = 0
            mp2[ch] += 1

        res = []
        # print(mp1)
        for idx, ch in enumerate(s[len(p):]):
            # print(mp2)
            if mp1 == mp2:
                res.append(idx)

            mp2[s[idx]] -= 1
            if mp2[s[idx]] == 0:
                del mp2[s[idx]]

            if ch not in mp2:
                mp2[ch] = 0
            mp2[ch] += 1

        if mp1 == mp2:
            res.append(len(s) - len(p))

        return res