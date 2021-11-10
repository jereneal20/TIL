class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ret = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    store_i = i
                    min_coord = (i, j)

                    while i != len(land) and land[i][j] == 1:
                        i += 1
                    i -= 1
                    while j != len(land[0]) and land[i][j] == 1:
                        j += 1
                    j -= 1

                    max_coord = (i, j)
                    ret.append([min_coord[0], min_coord[1], max_coord[0], max_coord[1]])
                    self.clean_up_farm(land, ret[-1])
                    i = store_i

        return ret

    def clean_up_farm(self, land, coords):
        for i in range(coords[0], coords[2] + 1):
            for j in range(coords[1], coords[3] + 1):
                land[i][j] = 0

    def findFarmland2(self, land: List[List[int]]) -> List[List[int]]:
        ret = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    max_coord = self.recursion(land, i, j)
                    ret.append([i, j, max_coord[0], max_coord[1]])
        return ret

    def recursion(self, land, i, j):
        if i < 0 or j < 0 or i >= len(land) or j >= len(land[0]):
            return (-1, -1)
        if land[i][j] == 0:
            return (-1, -1)

        land[i][j] = 0

        max_coord = (i, j)
        lis = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
        for elem in lis:
            coord = self.recursion(land, elem[0], elem[1])
            if sum(coord) > sum(max_coord):
                max_coord = coord

        return max_coord