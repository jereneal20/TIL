class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = 0

        idx_a, idx_b = len(a) - 1, len(b) - 1
        carry = 0
        res = ""
        while idx_a >= 0 or idx_b >= 0:
            a_num = int(a[idx_a]) if idx_a >= 0 else 0
            b_num = int(b[idx_b]) if idx_b >= 0 else 0

            if (a_num + b_num + carry) % 2 == 0:
                res += "0"
            else:
                res += "1"

            if a_num + b_num + carry >= 2:
                carry = 1
            else:
                carry = 0

            idx_a -= 1
            idx_b -= 1
        if carry == 1:
            res += "1"

        return res[::-1]