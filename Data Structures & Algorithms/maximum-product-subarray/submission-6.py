class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin = 1
        currMax = 1

        for num in nums:
            t = currMax*num
            currMax = max(currMax*num, num*currMin, num)
            currMin = min(t, num*currMin, num)
            res = max(currMax, res)
        return res