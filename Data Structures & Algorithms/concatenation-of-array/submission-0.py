class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = []
        def addition(output , nums):
            for i in nums:
                output.append(i)

        addition(output , nums)
        addition(output , nums)
        return output