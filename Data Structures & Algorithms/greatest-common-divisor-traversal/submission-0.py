class UnionFind:
    def __init__(self , n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self , x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self , x , y):
        px , py = self.find(x) , self.find(y)
        if px == py:
            return False
        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]

        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factor_idx = {}
        for i , n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_idx:
                        uf.union(i , factor_idx[f])
                    else:
                        factor_idx[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factor_idx:
                    uf.union(i , factor_idx[n])
                else:
                    factor_idx[n] = i
        return uf.count == 1

