class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefixSum = 0
        preMap = { 0:1 }
        for num in nums:
            prefixSum += num

            target = prefixSum - k 
            result += preMap.get(target, 0)

            preMap[prefixSum] = 1 + preMap.get(prefixSum, 0)
        return result