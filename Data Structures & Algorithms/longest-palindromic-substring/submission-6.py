class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left , right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left , right)
        
        res = ''
        for i in range(len(s)):
            (l1 , r1) = expand_around_center(i , i)
            if r1 - l1 - 1 > len(res):
                res = s[l1 + 1 : r1]
            (l2 , r2) = expand_around_center(i , i + 1)
            if r2 - l2 - 1 > len(res):
                res = s[l2 + 1 : r2]
        return res