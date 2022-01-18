class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return a | b
        # if (a < 0) ^ (b < 0):
        #     if a < 0:
        #         a = ~self.getSum(~a, 1)
        #     else:
        #         b = ~self.getSum(~b, 1)
        mask = 0xffffffff
        while b != 0:
            xor = (a ^ b) & mask
            an = ((a & b) << 1) & mask

            a = xor
            b = an

        if (a >> 31) & 1:  # If a is negative in 32 bits sense
            return ~(a ^ mask)
        return a