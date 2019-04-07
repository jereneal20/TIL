class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int i,j,tmp, pnt;
        for(i=0;i<A.size();i++) {
            for(j=0;j<(A[i].size()+1)/2;j++) {
                pnt = A[i].size()-j-1;
                tmp = A[i][j];
                A[i][j] = A[i][pnt];
                A[i][pnt] = tmp;
                A[i][j] ^= 1;
                if(j == pnt) continue;
                A[i][pnt] ^= 1;
            }
        }
        return A;
    }
};
