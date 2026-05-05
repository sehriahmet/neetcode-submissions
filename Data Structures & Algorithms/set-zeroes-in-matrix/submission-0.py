class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        i_list = set()
        j_list = set() 

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    i_list.add(row)
                    j_list.add(col)
        print(i_list, j_list)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in i_list or col in j_list: 
                    matrix[row][col] = 0
        