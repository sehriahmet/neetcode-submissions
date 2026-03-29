class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        visited = [] 
        que = []
        def add(i, j):
            if [i, j] in visited or i<0 or j<0 or i>=len(grid) or j >= len(grid[0]) or grid[i][j] == -1:
                return
            que.append([i, j])
            visited.append([i, j])
        def bfs():
            dist = 0
            while len(que) != 0:
                for k in range(len(que)): 
                    print(que)
                    i, j = que.pop(0)
                    grid[i][j] = dist
                    add(i-1, j)
                    add(i, j-1)
                    add(i+1, j)
                    add(i, j+1)
                dist += 1



        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    add(i, j)
        bfs()

