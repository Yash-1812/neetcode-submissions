class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        reversed_s = ''
        new_s = ''
        for i in range(len(s)):
            if s[i].isalnum():
                new_s = new_s + s[i]
        for i in range(len(s) - 1 , -1 , -1):
            if s[i].isalnum():
                reversed_s = reversed_s + s[i]
        return reversed_s == new_s