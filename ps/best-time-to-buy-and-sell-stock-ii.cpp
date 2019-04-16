class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i,j=0,res=0;
        for (i=1;i<prices.size();i++){
            if (prices[j] < prices[i]) {
                res+=prices[i]-prices[j];
            }
            j = i;
        }
        return res;
    }
};
