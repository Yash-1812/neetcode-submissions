class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        l = 1
        for i in range(1 , len(s)):
            ch = s[i]
            l = max(l , i - left)
            while ch in s[left:i]:
                left += 1
        return max(l , len(s) - left)