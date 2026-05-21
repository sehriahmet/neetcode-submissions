class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1 2 2 3 3 4 4 5
        # 1 2 3 4 5 
        n = len(nums)
        if n < 2:
            return n

        l = 0
        r = 1

        while l < n and r < n:
            # print(l, r, nums[l], nums[r], nums)
            if nums[r] > nums[l]:
                l = r
                r += 1
            else:
                temp = r
                while r < n and nums[r] <= nums[l]:
                    # print(l, r)
                    r += 1
                # print(r)
                if r < n:
                    nums[temp] = nums[r]
                    l = temp 
                    r = temp + 1
                else: 
                    break 
        
        return l+1


