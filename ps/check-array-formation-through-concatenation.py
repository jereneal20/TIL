class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces.sort()
        idx = 0
        while idx < len(arr):
            piece = self.findPieceStartingWithNum(pieces, arr[idx])
            if piece == None:
                return False
            for pick in piece:
                if pick != arr[idx]:
                    return False
                idx += 1
        return True

    def findPieceStartingWithNum(self, sortedPieces, num):
        start = 0
        end = len(sortedPieces) - 1
        while start <= end:
            mid = (int)((start + end) / 2)
            if sortedPieces[mid][0] == num:
                return sortedPieces[mid]
            if sortedPieces[mid][0] < num:
                start = mid + 1
            else:
                end = mid - 1
        return None

#                 [0 1 2 3, 4, 5, 6]


#         for pieces in sortedPieces:
#             if pieces[0] == num:
#                 return pieces
#         return None
