class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 1
        res = [0]
        while i <= n:
            # num = i
            # count = 0
            if i%2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[i//2]+1)
            # while num != 0:
            #     count = count+1 if num%2 == 1 else count
            #     num //= 2
            # res.append(count)
            i += 1
        return res