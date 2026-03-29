class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        for i in range(n):
            adj.append([])
        visited = []
        result = 0

        for i, j in edges: 
            adj[i].append(j)
            adj[j].append(i) 

        def dfs(node):
            if node in visited: 
                return 

            visited.append(node)
            for i in adj[node]: 
                dfs(i)
            # if idx < len(edges)-1 and edges[idx+1][0] == edges[idx][1]: 
            #     dfs(idx+1)
            # dfs(idx) TODO 
            
        for i in range(n):
            if i not in visited: 
                result += 1
                dfs(i) 
                print(visited, i)
        return result 
