class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        n = len(temperatures)
        for i in range(n - 1):
            curr = temperatures[i]
            visit = False
            for j in range(i + 1 , n):
                if temperatures[j] > curr:
                    visit = True
                    output.append(j - i)
                    break
            if not visit:
                output.append(0)
        output.append(0)
        return output
