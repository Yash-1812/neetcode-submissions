class Solution:
    def subsets(self , nums , k , idx , part , output):
        if len(part) == k:
            output.append(part.copy())
            return
        if idx >= len(nums):
            return
        part.append(nums[idx])
        self.subsets(nums , k , idx + 1 , part , output)
        part.pop()
        self.subsets(nums , k , idx + 1 , part , output)

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1 , n + 1)]
        output = []
        self.subsets(nums , k , 0 , [] , output)
        return output