class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        def rec(i):
            if i<=3:
                dp[i] = i
                return i
            if dp[i] > 0: 
                return dp[i]
            dp[i] = rec(i-1) + rec(i-2)
            return dp[i]
        return rec(n)