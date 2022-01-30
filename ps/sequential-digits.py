class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        st = "123456789"
        res = []
        for count in range(len(str(low)), len(str(high)) + 1):
            for i in range(9):
                if i + count <= 9 and low <= int(st[i:i + count]) <= high:
                    res.append(int(st[i:i + count]))
        return res
