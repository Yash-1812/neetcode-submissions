class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n == 2:
            return 1
        
        if n == 3:
            return 2

        if n % 3 == 0:
            return int(3 ** (n / 3))

        if n % 3 == 1:
            temp = 3 ** ((n - 4) / 3)
            return int(temp * 4)

        if n % 3 == 2:
            temp = 3 ** ((n - 2) / 3)
            return int(temp * 2)