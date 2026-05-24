class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False 
        start = 0 
        end = k
        hset = set()
        n = len(nums)

        for i in range(k+1):
            if i == n:
                return False

            if nums[i] in hset: 
                return True 

            hset.add(nums[i])
        # hset.remove(nums[start])
        # start += 1
        # end += 1
        while end < n - 1:
            # print(hset, k, start,end)
            hset.remove(nums[start])
            start += 1

            end += 1 
            if nums[end] in hset: 
                return True 
            hset.add(nums[end])
            
        return False