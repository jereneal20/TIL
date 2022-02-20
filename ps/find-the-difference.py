class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_mp = defaultdict(int)
        t_mp = defaultdict(int)
        for ch in s:
            s_mp[ch] += 1

        for ch in t:
            t_mp[ch] += 1

        print(s_mp)
        print(t_mp)

        res = ""
        for ch in t_mp:

            for i in range(t_mp[ch] - s_mp[ch]):
                res += ch

        return res

