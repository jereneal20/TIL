#include <limits.h>

class Solution {
public:
    int numSquares(int n) {
        int i,j,res=0,sum=0;        
        vector<int> square_nums(n+1,INT_MAX-1);
        if (n<=0) return 0;
        square_nums[0] = 0;
        for(i=1;i<=n;i++) {
            for(j=1;j*j<=i;j++) {
                square_nums[i] = min(square_nums[i], square_nums[i-j*j]+1);
            }
        }
        return square_nums[n];
    }
};
