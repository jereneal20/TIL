class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int i, res, buy_prev, sell_prev, buy, sell;
        if (prices.size() == 0 || prices.size() == 1) return 0;
        buy_prev = -fee - prices[0];
        sell_prev = 0;
        for(i=1;i<prices.size();i++) {
            buy = max(buy_prev, sell_prev-fee-prices[i]);
            sell = max(buy_prev+prices[i], sell_prev);
            buy_prev = buy;
            sell_prev = sell;
        }
        return max(buy, sell);
    }
};
