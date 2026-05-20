class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        delete_counts_left , delete_counts_right = 0 , 0
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                delete_counts_right += 1
                right -= 1
        left , right = 0 , len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                delete_counts_left += 1
                left += 1
        
        delete_counts = min(delete_counts_left , delete_counts_right)
        
        return delete_counts <= 1