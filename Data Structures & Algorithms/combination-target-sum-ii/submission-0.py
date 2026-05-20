class Solution:
    def getAnswers(self, candidates, target, subset, result, idx):
        if target == 0:
            result.append(subset.copy())
            return
        
        for i in range(idx, len(candidates)):
            # Skip duplicates at the same level
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            
            # Early stopping
            if candidates[i] > target:
                break
            
            subset.append(candidates[i])
            self.getAnswers(candidates, target - candidates[i], subset, result, i + 1)
            subset.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.getAnswers(candidates, target, [], result, 0)
        return result