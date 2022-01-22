class Solution:
    def originalDigits(self, s: str) -> str:

        # zero - z
        # one - o after zwu
        # two - w
        # three - h after g
        # four - u
        # five - f after u
        # six - x
        # seven - s after x
        # eight - g
        # nine - rest
        counts = [0] * 10
        counts[0] = s.count('z')
        counts[2] = s.count('w')
        counts[4] = s.count('u')
        counts[6] = s.count('x')
        counts[8] = s.count('g')

        counts[1] = s.count('o') - counts[0] - counts[2] - counts[4]
        counts[3] = s.count('h') - counts[8]
        counts[5] = s.count('f') - counts[4]
        counts[7] = s.count('s') - counts[6]
        counts[9] = s.count('i') - counts[8] - counts[6] - counts[5]

        res = ""
        for idx, count in enumerate(counts):
            if count == 0:
                continue
            for time in range(count):
                res += str(idx)
        return res