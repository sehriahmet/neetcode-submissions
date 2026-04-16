class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        result = []
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1
        # print(hmap)
        for i in range(k):
            m = nums[0]
            for key in hmap:
                if hmap[key] > hmap[m]: 
                    m = key
            hmap[m] = 0
            result.append(m)

        return result