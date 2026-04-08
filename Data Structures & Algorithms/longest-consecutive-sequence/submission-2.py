class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {} 
        res = 0
        for i in nums:
            if i not in hmap:
                hmap[i] = hmap.get(i+1, 0) + hmap.get(i-1, 0) + 1
                if hmap.get(i-1, -1) != -1: hmap[i - hmap[i-1]] = hmap[i]
                if hmap.get(i+1, -1) != -1: hmap[i + hmap[i+1]] = hmap[i]
                res = max(res, hmap[i])
        return res