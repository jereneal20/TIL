class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_mp = defaultdict(int)
        for ch in s1:
            s1_mp[ch] += 1

        i = 0
        while i < len(s1):
            s1_mp[s2[i]] -= 1
            if s1_mp[s2[i]] == 0:
                del s1_mp[s2[i]]
            i += 1

        while i < len(s2):
            if len(s1_mp) == 0:
                return True

            s1_mp[s2[i - len(s1)]] += 1
            if s1_mp[s2[i - len(s1)]] == 0:
                del s1_mp[s2[i - len(s1)]]
            s1_mp[s2[i]] -= 1
            if s1_mp[s2[i]] == 0:
                del s1_mp[s2[i]]
            i += 1
        if len(s1_mp) == 0:
            return True
        return False

