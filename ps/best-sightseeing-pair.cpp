class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int i,j, res = 0;
        i=0;
        for(j=1;j<A.size();j++) {
            if (A[j-1]+(j-i)>A[i]) i = j-1;
            res = max(res, A[i]+A[j]+i-j);
        }
        return res;
    }
};
