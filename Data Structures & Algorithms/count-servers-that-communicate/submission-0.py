class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0 
        row_counts = {}
        col_counts = {}
        counted_indices = []
        for i in range (len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: 
                    row_counts[i] = 1 + row_counts.get(i, 0) 

        for i in range(0, len(grid)): 
            if row_counts.get(i, 0) > 1: 
                count += row_counts[i]
                for j in range(0, len(grid[i])):
                    if grid[i][j] == 1: 
                        grid[i][j] = '#'
                        counted_indices.append([i, j])

        for i in range (len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 or grid[i][j] == '#': 
                    col_counts[j] = 1 + col_counts.get(j, 0)

        for i in range (len(grid)):
            for j in range(len(grid[i])):
                if col_counts.get(j, 0) > 1 and grid[i][j] == 1: 
                    count += 1 

        return count 