class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            visit = False
            for j in range(i + 1 , len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output.append(j - i)
                    visit = True
                    break
            if not visit:
                output.append(0)
        return output

