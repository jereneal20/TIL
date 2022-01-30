class WordDictionary:

    def __init__(self):
        self.mp = {}

    def addWord(self, word: str) -> None:
        mp = self.mp

        for ch in word:
            if ch not in mp:
                mp[ch] = {}
            mp = mp[ch]
        mp['$'] = {}

    def search(self, word: str) -> bool:
        mp = self.mp

        def recurse(mp, word, idx):
            res = False
            ch = word[idx]
            if ch == '$' and ch in mp:
                return True
            if ch == '.':
                for c in mp:
                    res |= recurse(mp[c], word, idx + 1)
            else:
                if ch in mp:
                    res |= recurse(mp[ch], word, idx + 1)

            return res

        return recurse(mp, word + '$', 0)


class WordDictionary2:

    def __init__(self):
        self.mp = {}

    def addWord(self, word: str) -> None:
        mp = self.mp
        n = len(word)
        for idx, ch in enumerate(word):
            if idx not in self.mp:
                self.mp[idx] = {}
            if n not in mp[idx]:
                mp[idx][n] = {}
            if ch not in mp[idx][n]:
                self.mp[idx][n][ch] = []

            mp[idx][n][ch].append(word)

    def search(self, word: str) -> bool:
        mp = self.mp
        n = len(word)
        candidates = []
        for idx, ch in enumerate(word):
            if ch != '.' and idx in mp and n in mp[idx] and ch in mp[idx][n]:
                candidates.append(mp[idx][n][ch])
                continue
            if ch == '.' and idx in mp and n in mp[idx]:
                cand = set()
                for ch in mp[idx][n]:
                    cand.update(mp[idx][n][ch])
                candidates.append(list(cand))
                continue
            return False
        # print(candidates)
        if len(candidates) == 0:
            return False
        candid_set = set(candidates[0])
        for candidate in candidates:
            candid_set.intersection_update(candidate)
            if len(candid_set) == 0:
                return False
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)