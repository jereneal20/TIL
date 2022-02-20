class RandomizedCollection:

    def __init__(self):
        self.map = defaultdict(dict)
        self.lis = []

    def insert(self, val: int) -> bool:
        ret = True
        if val in self.map and len(self.map[val]) != 0:
            ret = False
        self.lis.append(val)
        self.map[val][len(self.lis) - 1] = 1  # store index on the list
        return ret

    def remove(self, val: int) -> bool:
        if val not in self.map or len(self.map[val]) == 0:
            return False

        # get item to remove in map
        idx_to_remove, _ = self.map[val].popitem()
        self.map[val][idx_to_remove] = 1

        last_idx = len(self.lis) - 1

        del self.map[val][idx_to_remove]
        self.lis[idx_to_remove] = self.lis[-1]

        self.map[self.lis[idx_to_remove]][idx_to_remove] = 1
        del self.map[self.lis[idx_to_remove]][last_idx]

        self.lis.pop()

        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.lis) - 1)
        return self.lis[idx]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()