class Solution:
    def swap(self , matrix , r , c , m , n , check):
        r_ = 0
        c_ = 0
        while r_ < m:
            if matrix[r_][c] == 0:
                r_ += 1
                continue
            matrix[r_][c] = 0
            check.append([r_ , c])
            r_ += 1
        while c_ < n:
            if matrix[r][c_] == 0:
                c_ += 1
                continue
            matrix[r][c_] = 0
            check.append([r , c_])
            c_ += 1

    def setZeroes(self, matrix: List[List[int]]) -> None:
        checked_list = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 and [i , j] not in checked_list:
                    self.swap(matrix , i , j , rows , cols , checked_list)
                    #checked_list.append([i , j])

        
        