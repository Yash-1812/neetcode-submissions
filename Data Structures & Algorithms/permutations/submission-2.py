class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_path = []
        visited = set()
        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(current_path.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                current_path.append(nums[i])
                backtrack(current_path)
                current_path.pop()
                visited.remove(i)
        backtrack([])
        return result