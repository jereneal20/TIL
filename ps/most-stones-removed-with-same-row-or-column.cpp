rowStones = dict()
columnStones = dict()
stonesDict = dict()
class Solution:
    
    def removeStones(self, stones: List[List[int]]) -> int:    
        for stone in stones:
            if stone[0] not in rowStones:
                rowStones[stone[0]] = []
            rowStones[stone[0]].append(stone[1])
            if stone[1] not in columnStones:
                columnStones[stone[1]] = []
            columnStones[stone[1]].append(stone[0])
            stonesDict[(stone[0],stone[1])] = 1
        islands = 0
#         for i, j in stones:
#             if (i,j) not in stonesDict:
#                 continue
#             self.recurse(i, j)
#             islands += 1
#         return len(stones) - islands;
    
        for i1, j1 in stones:
            if (i1,j1) not in stonesDict:
                continue
            stk = [(i1, j1)]
            islands += 1
            while len(stk) > 0:
                (i, j) = stk.pop(len(stk) -1)
                if (i, j) not in stonesDict:
                    continue
                del stonesDict[(i,j)]
                if i in rowStones:
                    for row in rowStones[i]:
                        stk.append((i, row))
                    del rowStones[i]
                if j in columnStones:
                    for col in columnStones[j]:
                        stk.append((col, j))
                    del columnStones[j]
        return len(stones) - islands;
        
    def recurse(self, i, j):
        if (i,j) not in stonesDict:
            return 
        # print ((i, j))
        del stonesDict[(i,j)]
        
        for row in rowStones[i]:
            self.recurse(i, row)
        for col in columnStones[j]:
            self.recurse(col, j)
