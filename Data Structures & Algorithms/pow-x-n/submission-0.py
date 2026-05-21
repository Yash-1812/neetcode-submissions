class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1
        if n > 0:
            for i in range(n):
                p = p * x
        else:
            for i in range(abs(n)):
                p = p * (1/x)
        return p