class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n = min(len(word1), len(word2))

        for i in range(n):
            res += word1[i] + word2[i]

        res += word1[i+1:] + word2[i+1:]

        return res