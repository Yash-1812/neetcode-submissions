from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        result = []
        
        # Initialize the boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            
            # 1. Traverse from Left to Right along the current Top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move top boundary down
            
            # 2. Traverse from Top to Bottom along the current Right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move right boundary left
            
            # 3. Traverse from Right to Left along the current Bottom row
            # (We check "top <= bottom" to ensure this row hasn't already been processed)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move bottom boundary up
                
            # 4. Traverse from Bottom to Top along the current Left column
            # (We check "left <= right" to ensure this column hasn't already been processed)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move left boundary right
                
        return result