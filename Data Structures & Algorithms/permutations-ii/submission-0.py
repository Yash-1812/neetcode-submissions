class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perms = []
        count = Counter(nums)
        def backtrack():
            if len(perms) == len(nums):
                result.append(perms.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perms.append(n)
                    count[n] -= 1
                    backtrack()
                    count[n] += 1
                    perms.pop()
        backtrack()
        return result