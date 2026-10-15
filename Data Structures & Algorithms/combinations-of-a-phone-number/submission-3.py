class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
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
        def backtrack(idx , curr_char):
            if idx == len(digits):
                res.append(curr_char)
                return
            for ch in digits_to_char[digits[idx]]:
                backtrack(idx + 1 , curr_char + ch)
        backtrack(0 , '')
        return res