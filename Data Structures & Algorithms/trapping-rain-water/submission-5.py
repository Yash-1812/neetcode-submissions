class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_height = [0] * n
        right_height = [0] * n
        vol = 0
        for i in range(1 , n):
            left_height[i] = max(left_height[i - 1] , height[i - 1])
        for i in range(n - 2 , -1 , -1):
            right_height[i] = max(right_height[i + 1] , height[i + 1])
        for i in range(n):
            vol += max(0,(min(left_height[i] , right_height[i]) - height[i]))
        return vol