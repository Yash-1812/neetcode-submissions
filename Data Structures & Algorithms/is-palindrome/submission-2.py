class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for ch in s:
            if ch.islower():
                new_s += ch
            elif ch.isupper():
                new_s += ch.lower()
            elif ch.isdigit():
                return False
            else:
                continue
        reverse = ""
        for i in range(len(new_s) - 1 , -1 , -1):
            reverse += new_s[i]
        return reverse == new_s
        
        