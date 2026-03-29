class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        visited = set()
        def dfs(index, i ,j):
            if (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or index >= len(word) 
                or board[i][j] != word[index] or (i, j) in visited):
                return False 
            visited.add((i, j))
            if board[i][j] == word[index]: 
                print(word[index], index, i, j, visited)

                if index == len(word) - 1:
                    return True 
                result = dfs(index+1, i-1, j) or dfs(index+1, i, j-1) or dfs(index+1, i, j+1) or dfs(index+1, i+1, j)
                visited.remove((i, j))
                return result 
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    result = result or dfs(0, i ,j)
        return result 
        