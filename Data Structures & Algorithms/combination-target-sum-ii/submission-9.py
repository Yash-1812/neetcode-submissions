class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []
        def dfs(subset , curr_target , start_idx):

            if curr_target == 0:
                result.append(subset.copy())
                return
            if curr_target < 0:
                return
            for i in range(start_idx , len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                dfs(subset , curr_target - candidates[i] , i + 1)
                subset.pop()
        dfs([] , target , 0)
        return result