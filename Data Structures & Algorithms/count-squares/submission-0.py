import math
# allPoints = []
class CountSquares:

    def __init__(self):
        self.allPoints = []
        self.hmap = {}

    def add(self, point: List[int]) -> None:
        self.allPoints.append(point)
        self.hmap[tuple(point)] = self.hmap.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        result = 0
        px = point[0]
        py = point[1]
        for x, y in self.allPoints:
            if px == x or py == y or abs(px - x) != abs(py - y):
                continue
            result += self.hmap.get(tuple((px, y)), 0) * self.hmap.get(tuple((x, py)), 0)
        return result