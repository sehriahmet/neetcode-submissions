class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def addSubsets(arr):
            if len(arr) == 0: 
                return 
            if sorted(arr) not in result:
                result.append(sorted(arr[::]))
            print(arr, result)
            x = arr[::]
            for i in range(0, len(arr)):
                arr.pop(i)
                addSubsets(arr)
                arr = x[::]
        addSubsets(nums)
        return result