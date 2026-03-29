class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cand = set()

        for i, j, k in triplets:
            if i <= target[0] and j <= target[1] and k<= target[2]:
                if i == target[0]: cand.add(0)
                if j == target[1]: cand.add(1)
                if k == target[2]: cand.add(2)
                
        return len(cand) == 3