class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        if len(s) != len(t): return False
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        for c in t:
            if c not in hmap:
                return False
            hmap[c] -= 1
            if hmap[c] < 0:
                return False
        return True