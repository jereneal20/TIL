#include <limits.h>

class Solution {
public:
    int sol;
    int numSquares(int n) {
        sol=INT_MAX;
        recursion(0, n, n);
        return sol;
    }
    
    void recursion(int depth, int n, int last) {
        int num,i;
        bool ret;
        if (depth >= sol || depth > 5) return;
        if (n == 0) {
            if (sol > depth) sol = depth;
        }
        // num = sqrt(n);
        num = min(last, (int)sqrt(n));
        while(num != 0){
            recursion(depth+1, n-num*num, num);
            num--;
        }
    }
    
    int numSquares2(int n) {
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
