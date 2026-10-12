class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expand_around_center(l , r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        for i in range(len(s)):
            res += expand_around_center(i , i)
            res += expand_around_center(i , i + 1)
        return res