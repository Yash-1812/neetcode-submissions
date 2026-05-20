class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        ptr1 = 0
        ptr2 = n - 1
        while 0 <= ptr1 < m and 0 <= ptr2 < n:
            if target > matrix[ptr1][ptr2]:
                ptr1 += 1
            elif target < matrix[ptr1][ptr2]:
                ptr2 -= 1
            elif target == matrix[ptr1][ptr2]:
                return True
        return False