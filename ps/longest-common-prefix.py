class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        numberOfWords = len(strs)
        if numberOfWords == 0:
            return ""
        oneOfLength = len(strs[0])

        for idx in range(oneOfLength):
            for idx2 in range(numberOfWords):
                if len(strs[idx2]) <= idx:
                    return "".join(res)
                if strs[0][idx] != strs[idx2][idx]:
                    return "".join(res)
            res.append(strs[0][idx])

        return "".join(res)