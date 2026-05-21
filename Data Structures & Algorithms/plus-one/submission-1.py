class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        def reverse(arr):
            left = 0
            right = len(arr) - 1
            while left <= right:
                arr[left] , arr[right] = arr[right] , arr[left]
                left += 1
                right -= 1
            return arr
        
        c = 0
        num = 0
        for i in range(len(digits) - 1 , -1 , -1):
            num += digits[i] * (10 ** c)
            c += 1
        
        num = num + 1
        output = []
        while num >= 1:
            temp = num % 10
            output.append(temp)
            num = num // 10

        return reverse(output)