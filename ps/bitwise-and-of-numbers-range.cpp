class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int i;
        int res = 0;
        for (i=31;i>=0;i--){
            if ((m >> i & 1) == (n >> i & 1)) {
                res += ((m >> i) & (n >> i) & 1) << i;
            } else {
                break;
            }
        }
        return res;
    }
};


