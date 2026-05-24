class Solution:
    def combinations(self , nums , output , k , idx , subset):
        if len(subset) == k:
            if subset not in output:
                output.append(subset.copy())
                return
        if idx == len(nums):
            return
        subset.append(nums[idx])
        self.combinations(nums , output , k , idx + 1 , subset)
        subset.pop()
        self.combinations(nums , output , k , idx + 1 , subset)

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1 , n + 1)]
        output = []
        self.combinations(nums , output , k , 0 , [])
        return output