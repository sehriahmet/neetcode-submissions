class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited =[]
        count = 0

        def dfs(i, j):

            if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]):
                return 0
            if grid[i][j] == '0' or [i, j] in visited: 
                return 0

            visited.append([i, j])
            print(i,j)
            dfs(i+1, j)
            dfs(i, j+1)
            if i!=0: dfs(i-1,j)
            if j!=0: dfs(i,j-1)

        for i in range(len(grid)):
            for j in range (len(grid[i])):
                if grid[i][j] == '1' and not [i, j] in visited: 
                    dfs(i, j)
                    print(visited)
                    count += 1

        return count 
