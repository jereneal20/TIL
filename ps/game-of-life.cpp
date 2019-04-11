class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int i,j;
        for (i=0;i<board.size();i++){
            for(j=0;j<board[0].size();j++) {
                int live = board[i][j] & 1;
                int neighbor = 0;
                if (i != 0 && j != 0) neighbor += board[i-1][j-1] & 1;
                if (i != board.size()-1 && j != board[0].size()-1) 
                    neighbor += board[i+1][j+1] & 1;
                if (i != 0 && j != board[0].size()-1)
                    neighbor += board[i-1][j+1] & 1;
                if (i != board.size()-1 && j != 0)
                    neighbor += board[i+1][j-1] & 1;
                if (i != 0) neighbor += board[i-1][j] & 1;
                if (j != 0) neighbor += board[i][j-1] & 1;
                if (i != board.size()-1) neighbor += board[i+1][j] & 1;
                if (j != board[0].size()-1) neighbor += board[i][j+1] & 1;
                
                if (live && neighbor < 2) continue;
                if (live && (neighbor == 2 || neighbor == 3 )) board[i][j] |= 2;
                if (live && neighbor > 3) continue;
                if (!live && neighbor == 3) board[i][j] |= 2;
            }
        }
        for (i=0;i<board.size();i++){
            for(j=0;j<board[0].size();j++) {
                board[i][j] >>= 1;
            }
        }
        
    }
};
