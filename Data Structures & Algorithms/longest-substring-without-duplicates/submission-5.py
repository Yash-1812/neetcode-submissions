class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1


        max_length , start = 0 , 0
        for i in range(1 , len(s)):
            if s[i] in s[start:i]:
                while s[i] in s[start:i]:
                    start += 1
            else:
                max_length = max(max_length , i - start + 1)

        return max(1 , max_length)