class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def rec(idx, curr, currTarget):
            nonlocal result
            # print(curr, currTarget)
            if currTarget == 0:
                result.append(curr[:])
                return 
            if currTarget < 0: 
                return 
            for i in range(idx, len(nums)):
                if nums[i] > currTarget: return
                curr.append(nums[i])
                rec(i, curr, currTarget - nums[i])
                curr.pop()
        rec(0, [], target)
        return result 

