class Solution:
    def reverseBits(self, n: int) -> int:
        s1 = str(bin(n))[2:]
        for i in range(32-len(s1)):
            s1 = "0" + s1

        return int(s1[::-1], 2)
