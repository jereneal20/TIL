class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> res(A.size(), 0);
        int i, odd_idx=1, even_idx=0;
        
        for(i=0;i<A.size();i++) {
            if (A[i] % 2 == 0){
                res[even_idx] = A[i];
                even_idx+=2;
            } else {
                res[odd_idx] = A[i];
                odd_idx+=2;
            }
        }
        return res;
    }
};
