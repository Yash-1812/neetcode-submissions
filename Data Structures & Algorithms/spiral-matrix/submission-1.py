class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        m , n = len(matrix) , len(matrix[0])
        left , right = 0 , n - 1
        top , bottom = 0 , m - 1
        while left <= right and top <= bottom:
            for c in range(left , right + 1 , 1):
                output.append(matrix[top][c])
            top += 1
            for r in range(top , bottom + 1 , 1):
                output.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for c in range(right , left - 1 , -1):
                    output.append(matrix[bottom][c])
                
                bottom -= 1
            if left <= right:
                for r in range(bottom , top - 1 , -1):
                    output.append(matrix[r][left])
                left += 1
        return output