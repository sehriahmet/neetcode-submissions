class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bought = -1;
        int profit = 0;
        for (int i = 0; i < prices.size()-1; i++) {
            if (bought == -1) {
                if (prices[i] < prices[i+1]) {
                    bought = i;
                }
            } else {
                if (prices[i] > prices[i+1]) {
                    profit += (prices[i] - prices[bought]);
                    bought = -1;
                }
            }
        }

        if (bought != -1) {
            profit += prices[prices.size()-1] - prices[bought];
        }

        return profit;
    }
};