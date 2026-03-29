class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)
        count = 0
        for i in range(len(str(a))):
            if a[i] == '1': 
                count+=1

        return count