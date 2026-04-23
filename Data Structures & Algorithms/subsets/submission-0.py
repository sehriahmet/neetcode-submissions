import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def rec(arr):
            if arr in result:
                return
            result.append(arr)
            for i in range(len(arr)):
                tmp = copy.copy(arr)
                tmp.remove(arr[i])
                rec(tmp)
        rec(nums)
        return result