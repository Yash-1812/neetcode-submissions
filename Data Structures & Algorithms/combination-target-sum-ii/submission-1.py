class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        candidates.sort()

        def combinations(start_idx , curr_target , subset):
            if curr_target == 0:
                output.append(subset.copy())
                return
            if curr_target < 0:
                return
            for i in range(start_idx , len(candidates)):
                if candidates[i] > curr_target:
                    break
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                combinations(i + 1 , curr_target - candidates[i] , subset)
                subset.pop()
        combinations(0 , target , [])
        return output
