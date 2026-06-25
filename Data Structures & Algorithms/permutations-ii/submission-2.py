class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        count = Counter(nums)

        def dfs(sub):
            if len(sub) == len(nums):
                result.append(sub.copy())
                return
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    sub.append(n)
                    dfs(sub)
                    sub.pop()
                    count[n] += 1
        
        dfs([])
        return result
