class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last_idx = dict()
        for i, c in enumerate(text):
            last_idx[c] = i
        
        res = []
        for i, c in enumerate(text):
            if c not in res:
                while len(res) > 0 and res[-1] > c and last_idx[res[-1]] > i:
                    del res[-1]
                res.append(c)
        
        return "".join(res)
