class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1:
            visit.add(n)
            s = 0
            while n >= 1:
                temp = n % 10
                s += temp ** 2
                n = n // 10
            n = s
            if n in visit:
                return False
        return True