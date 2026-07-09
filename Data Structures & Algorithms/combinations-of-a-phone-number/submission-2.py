class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digits_to_char = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        def backtrack(i , curr_str):
            if len(curr_str) == len(digits):
                result.append(curr_str)
                return
            ch = digits[i]
            for c in digits_to_char[ch]:
                backtrack(i + 1 , curr_str + c)
        if digits:
            backtrack(0 , '')
        return result