class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visit = set()

        def dfs(subset):
            if len(nums) == len(subset):
                result.append(subset.copy())
                return
            for i in range(len(nums)):
                if i in visit:
                    continue
                subset.append(nums[i])
                visit.add(i)
                dfs(subset)
                subset.pop()
                visit.remove(i)
        dfs([])
        return result
