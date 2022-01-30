class Solution:
    # Think about it as a tree again.
    # https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/1345905/C%2B%2BPython-Trie-Solution-Clean-and-Concise-O(32N)
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            found = set([num & mask for num in nums])
            start = ans | 1<<i

            for pref in found:
                if start ^ pref in found:
                    ans = start
                    break
        return ans