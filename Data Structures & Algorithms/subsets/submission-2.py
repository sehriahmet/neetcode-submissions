class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, curr):
            result.append(curr[:])
            temp = nums[idx:]
            for i in range(len(temp)):
                curr.append(temp[i])
                backtrack(idx+i+1, curr)
                curr.pop()

        backtrack(0, [])
        return result