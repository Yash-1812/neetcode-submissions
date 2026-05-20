class Solution:
    def transpose(self , matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i , cols):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        

    def rotate(self, matrix: List[List[int]]) -> None:
        #row_size = len(matrix)
        #self.transpose(matrix)
        left = 0
        right = len(matrix) - 1 
        while left <= right:
            matrix[left] , matrix[right] = matrix[right] , matrix[left]
            left += 1
            right -= 1
        self.transpose(matrix)
            
