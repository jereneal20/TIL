class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prev_buy, prev_sell, prev_rest;
        int buy, sell, rest;
        int i;
        if (prices.size() == 0) return 0;
        if (prices.size() == 1) return 0;
        prev_buy = -prices[0];
        prev_sell = 0;
        prev_rest = 0;
        for (i=1;i<prices.size();i++) {
            buy = max(prev_rest-prices[i], prev_buy);
            sell = prev_buy+prices[i];
            rest = max(prev_sell, prev_rest);
            prev_buy = buy;
            prev_sell = sell;
            prev_rest = rest;
        }
        return max(sell, rest);
    }
};
