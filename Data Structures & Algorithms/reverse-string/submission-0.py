class Solution:
    def reverseString(self, s: List[str]) -> None:
        r = len(s) - 1
        l = 0
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            r -= 1 
            l += 1
        
        