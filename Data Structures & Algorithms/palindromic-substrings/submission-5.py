class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expand_around_center(left , right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        for i in range(len(s)):
            l1 = expand_around_center(i , i)
            l2 = expand_around_center(i , i + 1)
            res += l1 + l2
        return res