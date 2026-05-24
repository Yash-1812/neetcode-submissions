class Solution:
    def combinations(self , nums , k , idx , subset , output):
        if len(subset) == k:
            if subset not in output:
                output.append(subset.copy())
        if idx == len(nums):
            return
        subset.append(nums[idx])
        self.combinations(nums , k , idx + 1 , subset , output)
        subset.pop()
        self.combinations(nums , k , idx + 1 , subset , output)

    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        nums = [i for i in range(1 , n + 1)]
        self.combinations(nums , k , 0 , [] , output)
        return output