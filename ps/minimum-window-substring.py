class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 필요한 것들의 개수를 담아둔 맵과 이게 만족했는지 한번에 체크해주는 변수 하나.
        # 맵에 현재 개수를 넣는게 아니라 t에 있는걸 넣은 상태에서 모든 수가 0 미만이면 조건을 만족하는걸 보는거다. 변수 하나는 이걸 빨리 볼 수 있게 해주는거고.
        # https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
        def every_t_in_s(s_mp, t_mp):
            for t_ch in t_mp:
                if t_ch not in s_mp:
                    return False
                if s_mp[t_ch] < t_mp[t_ch]:
                    return False
                # It's ok to have such a s_ch not exist in t_ch
            return True

        t_mp = defaultdict(int)
        for ch in t:
            t_mp[ch] += 1

        min_length = len(s) + 10
        min_tuple = None
        s_mp = defaultdict(int)
        i, j = 0, -1
        while i < len(s):
            s_mp[s[i]] += 1

            while every_t_in_s(s_mp, t_mp):
                if min_length >= i - j:
                    min_length = i - j
                    min_tuple = (j, i)
                j += 1
                s_mp[s[j]] -= 1

                if not every_t_in_s(s_mp, t_mp):
                    s_mp[s[j]] += 1
                    j -= 1
                    break
            i += 1

        if not min_tuple:
            return ""
        return s[min_tuple[0] + 1:min_tuple[1] + 1]


