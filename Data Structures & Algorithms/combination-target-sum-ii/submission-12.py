class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        part = []
        candidates.sort()
        def backtrack(curr_target , idx):
            if curr_target < 0 or idx > len(candidates):
                return
            if curr_target == 0:
                result.append(part.copy())
                return
            for i in range(idx , len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                part.append(candidates[i])
                backtrack(curr_target - candidates[i] , i + 1)
                part.pop()
        backtrack(target , 0)
        return result