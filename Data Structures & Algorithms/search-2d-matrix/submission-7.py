class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i , j = 0 , n - 1
        while i < m and j >= 0:
            num = matrix[i][j]
            if num < target:
                i += 1
            elif num > target:
                j -= 1
            elif num == target:
                return True
        return False 