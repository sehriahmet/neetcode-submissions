class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[]
        
        for i in range (0,k):
            arr.append(nums[i])
        result = min(arr)
        arr.pop(arr.index(result))
        for i in range(k, len(nums)):
            if nums[i] > result:
                arr.append(nums[i])
                result = min(arr)
                arr.pop(arr.index(result))
        return result 
