class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        if (n < 0) {
            x = 1/x;
            n = -1 * (long) n;
        }
        int i;
        double res = 1;
        double arr[32] = {0};
        arr[0] = x;
        for(i=1;i<32;i++) {
            arr[i] = arr[i-1]*arr[i-1];
        }
        for (i=0;i<32;i++) {
            res *= n % 2 ? arr[i]: 1;
            n >>= 1;
        }
        return res;
    }
};
