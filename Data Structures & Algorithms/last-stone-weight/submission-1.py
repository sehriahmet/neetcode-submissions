class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones = sorted(stones)
            x, y = stones[-2], stones[-1]
            if x == y:
                stones = stones[:-2]
            if x < y:
                stones = stones[:-2]
                stones.append(y - x)
        if stones: return stones[0]
        else: return 0 
