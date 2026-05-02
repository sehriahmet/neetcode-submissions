class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        expected = 0
        for i in range(len(nums)):
            if expected not in nums:
                return expected
            expected += 1
        return expected