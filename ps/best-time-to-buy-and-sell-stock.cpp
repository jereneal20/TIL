class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i,j=0, res = 0;
        for(i=0;i<prices.size();i++) {
            if (prices[i] < prices[j]) j = i;
            res = max(res, prices[i] - prices[j]);
        }
        return res;
    }
};
