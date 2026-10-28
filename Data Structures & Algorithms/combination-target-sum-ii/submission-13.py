class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        part = []
        def backtrack(idx , curr_target):
            if curr_target == 0:
                res.append(part.copy())
                return
            if curr_target < 0 or idx == len(candidates):
                return
            for i in range(idx , len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                part.append(candidates[i])
                backtrack(i + 1 , curr_target - candidates[i])
                part.pop()
        backtrack(0 , target)
        return res