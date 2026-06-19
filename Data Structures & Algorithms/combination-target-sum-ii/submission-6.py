class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates = sorted(candidates)
        def backtrack(start_idx , curr_target , subset):
            if curr_target == 0:
                result.append(subset.copy())
                return
            if curr_target < 0:
                return
            for i in range(start_idx , len(candidates)):
                if start_idx < i and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(i + 1 , curr_target - candidates[i] , subset)
                subset.pop()
        backtrack(0 , target , [])
        return result