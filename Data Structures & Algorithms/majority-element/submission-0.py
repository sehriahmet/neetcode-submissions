class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        n = len(nums)
        for num in nums: 
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
            if hmap[num] > n/2:
                return num
        return -1 # won't hit this part 