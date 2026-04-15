class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) +2)
        def rec(i):
            if i == 0:
                dp[0] = cost[0]
                return cost[0]
            if i == 1:
                return cost[1]
            if dp[i] > 0:
                return dp[i]
            dp[i] = min(rec(i-1), rec(i-2)) + cost[i]
            return dp[i]
        cost.append(0)
        return rec(len(cost)-1)
