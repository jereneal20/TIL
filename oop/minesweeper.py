"""
지뢰찾기를 구현하라.

"""
"""
input: board status, click
output: board status


- MineBoard
  - width, height
  - solution_board
  - current_board
  - 

solution_board
x10
121
01x

current_board
.10
.21
...

012345678x


1-8 : 
X : mine

E: unrevealed
M: unrevealed mine
X: revealed mine
1-8: reveled, adj mines
B: revealed blank


M1B
E21
EEM
"""



class Cell:
    is_open = False
    status = 0 # : 0-8, X
    

class MineBoard():

    def __init__(width, height, number_of_mines):
        self.width = width
        self.height = height
        board => 2 dimensional Cell objects
#        ...

def update_board_status(mine_board, click_event):
    x, y = click_event
    clicked_cell = mine_board[x][y]
    if clicked_cell.is_open == True:
        return
    clicked_cell.is_open = True
    if clicked_cell.status != 0:
	    return mine_board

    
   	# recursively open neighbors
    if x != 0:
        update_board_status(mine_board, (x-1, y))
    if x != mine_board.width - 1:
        update_board_status(mine_board, (x+1, y))
    if y != 0:
        update_board_status(mine_board, (x, y-1))
    if y != mine_board.height - 1:
        update_board_status(mine_board, (x, y+1))
        
    if x != 0 && y != 0:
        update_board_status(mine_board, (x-1, y-1))

	#...
    
    return mine_board
    
