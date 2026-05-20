class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for ch in operations:
            if ch == '+':
                num1 = scores.pop()
                num2 = scores.pop()
                num3 = int(num1) + int(num2)
                scores.append(num2)
                scores.append(num1)
                scores.append(str(num3))
                continue
            if ch == 'D':
                n = scores.pop()
                prod = int(n) * 2
                scores.append(n)
                scores.append(str(prod))
                continue
            if ch == 'C':
                scores.pop()
                continue
            scores.append(ch)
        s = 0
        for n in scores:
            s += int(n)
        return s