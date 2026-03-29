class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areas = [0]
        area = 0
        def dfs(i, j):
            if i<0 or j<0 or i>= len(grid) or j>= len(grid[i]):
                return 0 
            if grid[i][j] == '#' or grid[i][j] == 0: 
                return 0 

            grid[i][j] = '#'

            area = dfs(i+1, j)
            area += dfs(i, j+1)
            if i != 0: area += dfs(i-1, j)
            if j!=0: area += dfs(i,j-1) 

            return area + 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: 
                    areas.append(dfs(i, j))

        return max(areas)
            
