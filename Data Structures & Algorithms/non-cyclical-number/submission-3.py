class Solution:
    def find_sum(self , n):
        s = 0
        while n >= 1:
            temp = n % 10
            s += temp ** 2
            n = n // 10
        return s  
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visited = []
        d = n
        while d != 1:
            d = self.find_sum(d)
            if d == 1:
                return True
            
            if d not in visited:
                visited.append(d)
            else:
                return False