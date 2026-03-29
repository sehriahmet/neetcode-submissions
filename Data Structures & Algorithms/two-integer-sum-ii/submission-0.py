class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)-1
        r = 0

        while l>r: 
            if numbers[l] + numbers[r] == target:
                return [r+1, l+1]
            if numbers[l] + numbers[r] > target:
                l -=1
            elif numbers[l] + numbers[r] < target:
                r += 1
        return []