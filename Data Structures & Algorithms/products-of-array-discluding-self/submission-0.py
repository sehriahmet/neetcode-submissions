class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prev = 1
        temp1 = []
        temp2 = [1] * l
        temp1.append(1)
        for i in range(1, l):
            temp1.append(prev * nums[i-1])
            prev = temp1[i]
        prev = 1
        for i in range(l-2, -1, -1):
            temp2[i] = prev * nums[i+1]
            prev = temp2[i]
        for i in range(l):
            nums[i] = temp1[i] * temp2[i]
        return nums
