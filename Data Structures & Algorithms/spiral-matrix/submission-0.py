class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right -> down -> left -> up --> r
        row = len(matrix) # row size  
        col = len(matrix[0]) # col size 
        visited = set()
        result = []
        def go_right(i, j):
            while j < col and j >= 0 and (i, j) not in visited:
                result.append(matrix[i][j])
                visited.add((i, j))
                j += 1
            return (i, j - 1)
        def go_left(i, j):
            while j < col and j >= 0 and (i, j) not in visited:
                result.append(matrix[i][j])
                visited.add((i, j))
                j -= 1
            return (i, j + 1)
        def go_up(i, j):
            while i >= 0 and i < row and (i, j) not in visited:
                result.append(matrix[i][j])
                visited.add((i, j))
                i -= 1
            return (i + 1, j)
        def go_down(i, j):
            while i >= 0 and i < row and (i, j) not in visited:
                result.append(matrix[i][j])
                visited.add((i, j))
                i += 1
            return (i - 1, j)

        i, j = 0, 0
        while len(result) < row * col:
            i, j = go_right(i, j)
            i += 1

            i, j = go_down(i, j)
            j -= 1

            i, j = go_left(i, j)
            i -= 1

            i, j = go_up(i, j)
            j += 1
        return result


        