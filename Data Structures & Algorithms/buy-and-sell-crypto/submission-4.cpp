class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int l = 0;
        for (int  i = 1; i < prices.size(); i++) {
            if (prices[i] < prices[l]) {
                l = i;
                continue;
            }
            if (profit < prices[i] - prices[l]) profit = prices[i] - prices[l];
        }
        return profit;
    }
};
