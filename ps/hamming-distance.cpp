class Solution {
public:
    int hammingDistance(int x, int y) {
        int res=0,k;
        k=x^y;
        while(k!=0){
            if (k%2==1) res++;
            k >>= 1;
        }
        return res;
    }
};
