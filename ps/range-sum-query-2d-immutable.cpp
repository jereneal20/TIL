class NumMatrix {
private:
    vector<vector<int>> sumMatrix;
public:
    
    NumMatrix(vector<vector<int>> matrix) {
        int i,j, val = 0;
        // if (matrix.size() == 0) return;
        // sumMatrix = vector<vector<int>>(matrix.size(), vector<int>(matrix[0].size(), 0));
        for(i=0;i<matrix.size();i++){
            vector<int> res;
            sumMatrix.push_back(res);
            for(j=0;j<matrix[0].size();j++) {
                val = matrix[i][j];
                if (i != 0) val += sumMatrix[i-1][j];
                if (j != 0) val += sumMatrix[i][j-1];
                if (i != 0 && j != 0) val -= sumMatrix[i-1][j-1];
                sumMatrix[i].push_back(val);
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int val;
        val = sumMatrix[row2][col2];
        if (col1 != 0) val -= sumMatrix[row2][col1-1];
        if (row1 != 0) val -= sumMatrix[row1-1][col2];
        if (col1 != 0 && row1 != 0) val += sumMatrix[row1-1][col1-1];
        return val;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
