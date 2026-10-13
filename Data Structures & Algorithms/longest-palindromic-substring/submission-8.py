class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        ans = ''
        def expand_around_center(l , r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l , r)
        for i in range(len(s)):
            l1 , r1 = expand_around_center(i , i)
            if r1 - l1 - 1 > res:
                ans = s[l1 + 1 : r1]
                res = r1 - l1 - 1
            l2 , r2 = expand_around_center(i , i + 1)
            if r2 - l2 - 1 > res:
                ans = s[l2 + 1 : r2]
                res = r2 - l2 - 1
        return ans