class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = 0
        n = len(matrix[0]) - 1
        while 0 <= m < len(matrix) and 0 <= n < len(matrix[0]):
            if matrix[m][n] < target:
                m = m + 1
            elif matrix[m][n] > target:
                n = n - 1
            elif matrix[m][n] == target:
                return True
        return False
