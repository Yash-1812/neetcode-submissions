class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def binary_to_decimal(s):
            num = 0
            n = len(s) - 1
            for i in range(len(s) - 1 , -1 , -1):
                num += int(s[i]) * (2 ** (n - i))
            return num
        
        def decimal_to_binary(num):
            s = ""
            if num == 0:
                return "0"
            if num == 1:
                return "1"
            while num > 1:
                temp = num % 2
                s += str(temp)
                num = num // 2
            s += '1'
            return s[::-1]
        
        a_num = binary_to_decimal(a)
        b_num = binary_to_decimal(b)
        c = a_num + b_num
        return decimal_to_binary(c)