class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = defaultdict(set)
        check_col = defaultdict(set)
        check_square = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue 
                if (board[row][col] in check_row[row] 
                        or board[row][col] in check_col[col] 
                        or board[row][col] in check_square[row // 3, col // 3]): 
                    return False
                
                check_row[row].add(board[row][col])
                check_col[col].add(board[row][col])
                check_square[row//3, col//3].add(board[row][col])
        return True 
