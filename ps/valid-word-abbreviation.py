class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if abbr[j] == '0':
                return False

            if not abbr[j].isnumeric():
                return False
            k = j
            while j < len(abbr) and abbr[j].isnumeric():
                j += 1
            i += int(abbr[k:j])
        if i == len(word) and j == len(abbr):
            return True
        return False