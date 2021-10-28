class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        numOfDigits = 0
        dig = n
        while dig != 0:
            dig = (int)(dig / 10)
            numOfDigits += 1

        lis_n = list(str(n))
        idx = 0
        idx2 = 0
        while idx < len(lis_n) - 1:
            if lis_n[idx] <= lis_n[idx + 1]:
                idx += 1
                if lis_n[idx - 1] != lis_n[idx]:
                    idx2 = idx
                continue
            return n - (n % pow(10, len(lis_n) - idx2 - 1)) - 1

        return n
