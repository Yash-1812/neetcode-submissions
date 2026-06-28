class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        res = 0
        left , right = 0 , 1
        while right < len(s):
            if s[right] in s[left:right]:
                res = max(res , right - left)
                while s[right] in s[left:right]:
                    left += 1
            right += 1
        return max(res, right - left)
