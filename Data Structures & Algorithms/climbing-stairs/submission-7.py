class Solution:
    def climbStairs(self, n: int) -> int:
        a , b = 1 , 1
        for _ in range(n - 1):
            temp = a + b
            b = a
            a = temp
        return a