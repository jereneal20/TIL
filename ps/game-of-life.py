class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        prev_list = []
        for i in range(len(board)):
            curr_list = list(board[i])

            for j in range(len(board[i])):
                numOfLivingNeighbor = 0
                if i != 0:
                    numOfLivingNeighbor += prev_list[j]
                if j != 0:
                    numOfLivingNeighbor += curr_list[j - 1]
                if i != 0 and j != 0:
                    numOfLivingNeighbor += prev_list[j - 1]

                if i != len(board) - 1:
                    numOfLivingNeighbor += board[i + 1][j]
                if j != len(board[i]) - 1:
                    numOfLivingNeighbor += curr_list[j + 1]
                if i != len(board) - 1 and j != len(board[i]) - 1:
                    numOfLivingNeighbor += board[i + 1][j + 1]

                if i != 0 and j != len(board[i]) - 1:
                    numOfLivingNeighbor += prev_list[j + 1]
                if j != 0 and i != len(board) - 1:
                    numOfLivingNeighbor += board[i + 1][j - 1]

                if board[i][j] == 1:
                    if numOfLivingNeighbor < 2 or numOfLivingNeighbor > 3:
                        board[i][j] = 0
                else:
                    if numOfLivingNeighbor == 3:
                        board[i][j] = 1

            prev_list = curr_list

