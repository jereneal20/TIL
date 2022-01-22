class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        i = 0
        count = 0
        total_so_far = 0
        while count < len(gas):
            if i > len(gas) * 2:
                return -1
            total_so_far += gas[i % len(gas)] - cost[i % len(gas)]
            if total_so_far >= 0:
                i += 1
                count += 1
            else:
                total_so_far = 0
                i += 1
                count = 0
        return i % len(gas)