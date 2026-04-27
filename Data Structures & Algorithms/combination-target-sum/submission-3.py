class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def rec(curr, currTarget):
            nonlocal result
            # print(curr, currTarget)
            if currTarget == 0:
                if sorted(curr) not in result: result.append(curr[:])
                return 
            if currTarget < 0: 
                return 
            for i in nums:
                curr.append(i)
                rec(curr, currTarget - i)
                curr.pop()
        for i in nums:
            rec([i], target - i)
        return result 

