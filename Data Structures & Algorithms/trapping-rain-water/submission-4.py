class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        for i in range(1 , n):
            left_max[i] = max(height[i - 1] , left_max[i - 1])
        for i in range(n - 2 , -1 , -1):
            right_max[i] = max(height[i + 1] , right_max[i + 1])
        res = 0
        for i in range(n):
            if min(left_max[i] , right_max[i]) - height[i] < 0:
                continue
            res += min(left_max[i] , right_max[i]) - height[i]
        return res