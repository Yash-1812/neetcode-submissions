class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete_right , delete_left = 0 , 0
        left , right = 0 , len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                delete_right += 1
                right -= 1
        left , right = 0 , len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                delete_left += 1
                left += 1
        delete = min(delete_right , delete_left)
        return delete <= 1 