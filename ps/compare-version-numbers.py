class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splitted1 = version1.split('.')
        splitted2 = version2.split('.')
        i, j = 0, 0
        while i < len(splitted1) and i < len(splitted2):
            if int(splitted1[i]) > int(splitted2[i]):
                return 1
            elif int(splitted1[i]) < int(splitted2[i]):
                return -1
            i += 1

        while i < len(splitted1):
            if int(splitted1[i]) > 0:
                return 1
            i += 1

        while i < len(splitted2):
            if int(splitted2[i]) > 0:
                return -1
            i += 1
        return 0