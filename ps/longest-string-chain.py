class Solution:
    # https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        dp = {}
        longest = 1
        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1:]

                if prev_word in dp:
                    dp[word] = max(dp[prev_word] + 1, dp[word])
                    longest = max(dp[word], longest)
        return longest

    def longestStrChain2(self, words: List[str]) -> int:
        words.sort(key=len)

        arr = [[False] * len(words) for i in range(len(words))]
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                arr[i][j] = self.isPredecessor(words[i], words[j])

        max_count = 0
        self.cached_depth = [-1] * len(words)
        for i in range(len(words)):
            max_count = max(max_count, self.getLongestDepth(arr, i) + 1)

        return max_count

    def getLongestDepth(self, arr, i):
        length = 0
        if self.cached_depth[i] != -1:
            return self.cached_depth[i]
        for k in range(i + 1, len(arr)):
            if arr[i][k]:
                length = max(length, self.getLongestDepth(arr, k) + 1)

        self.cached_depth[i] = length
        return length

    def isPredecessor(self, val1, val2):
        if len(val1) + 1 != len(val2):
            return False
        i = 0
        while i < len(val1):
            if val1[i] != val2[i]:
                if val1[i:] == val2[i + 1:]:
                    return True
                return False
            i += 1
        return True
