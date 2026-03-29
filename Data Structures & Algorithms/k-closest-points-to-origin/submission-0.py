class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [] 
        result = []
        for i in range(len(points)): 
            distances.append([points[i][0]**2 + points[i][1]**2, points[i][0], points[i][1]])
        heapq.heapify(distances)
        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            result.append([x, y])
        return result
