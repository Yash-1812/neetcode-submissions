class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def number_of_ones(num):
            ones = 0
            result = ''
            if num == 0:
                return 0
            if num == 1:
                return 1
            while num > 1:
                temp = num % 2
                result += str(temp)
                num = num // 2
            result += str(1)
            for i in range(len(result)):
                if result[i] == '1':
                    ones += 1
            return ones

        output = []
        for i in range(n + 1):
            output.append(number_of_ones(i))
        return output
