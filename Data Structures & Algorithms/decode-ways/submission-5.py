class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} 
        memo[0] = 1
        
        if s[0] == "0":
            return 0

        def rec(idx):
            if idx >= len(s) or idx < 0: 
                return 0
            if idx in memo:
                return memo[idx]
            if idx == 1: 
                memo[1] = 1 + memo[0]
                if (int(s[idx-1]) == 2 and int(s[idx]) > 6) or int(s[idx-1]) > 2:
                    memo[1] = 1
                if s[idx] == "0":
                    if s[idx-1] not in "12":
                        memo[-1] = 0
                        return 0
                    memo[1] = memo[0]
                return memo[1]
            if s[idx] == "0":
                if s[idx-1] not in "12":
                    memo[-1] = 0
                    return 0
                else:
                    memo[idx] = rec(idx - 2)
                return memo[idx]
            if s[idx-1] != "0" and int(s[idx-1]) <= 2:
                if (int(s[idx-1]) == 2 and int(s[idx]) > 6) or int(s[idx-1]) > 2:
                    print("aa")
                    memo[idx] = rec(idx - 1)
                else: 
                    memo[idx] = rec(idx-1) + rec(idx - 2)
            else:
                memo[idx] = rec(idx - 1)
            return memo[idx]
        rec(len(s) - 1)
        print(memo)
        if -1 in memo: return 0
        return memo[len(s) - 1]