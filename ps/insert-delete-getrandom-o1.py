class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.lis = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.lis.append(val)
        self.map[val] = len(self.lis) - 1  # store index on the list
        return True

    def remove(self, val: int) -> bool:
        if not val in self.map:
            return False
        idx = self.map[val]
        self.lis[idx] = self.lis[-1]
        self.map[self.lis[-1]] = idx
        del self.map[val]
        self.lis.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.lis) - 1)
        return self.lis[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()