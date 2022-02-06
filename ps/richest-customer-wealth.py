class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_account = 0
        for account in accounts:
            max_account = max(max_account, sum(account))
        return max_account