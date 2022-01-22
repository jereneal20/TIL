class Solution:
    total = -1
    lis = []

    def __init__(self, w: List[int]):
        self.total = -1
        self.lis = []
        for weight in w:
            self.lis.append([weight, self.total+1, self.total+weight])
            self.total += weight
        # print(self.lis)
        # print(self.total)

    def pickIndex(self) -> int:
        picked = random.randint(0, self.total)
        l, r = 0, len(self.lis)
        while l < r:
            mid = (l+r)//2
            if self.lis[mid][1] <= picked <= self.lis[mid][2]:
                return mid
            elif picked < self.lis[mid][1]:
                r = mid
            else:
                l = mid + 1
        return mid

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()