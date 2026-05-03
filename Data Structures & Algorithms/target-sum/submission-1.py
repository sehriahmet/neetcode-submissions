class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def rec(idx, total):
            if (idx, total) in memo:
                return memo[(idx, total)]
            if idx == len(nums):
                if total == target: 
                    return 1 
                return 0 
            
            res = rec(idx + 1, total + nums[idx]) + rec(idx + 1, total - nums[idx])
            memo[(idx, total)] = res
            return res
        return rec(0, 0)