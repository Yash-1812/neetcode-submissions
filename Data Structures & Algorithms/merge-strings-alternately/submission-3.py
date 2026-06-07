class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 , ptr2 = 0 , 0
        i = 0
        n = len(word1) + len(word2)
        res = ""
        while i < n:
            if ptr1 == len(word1) and len(word2) > len(word1):
                res += word2[ptr2:]
                break
            elif ptr2 == len(word2) and len(word1) > len(word2):
                res += word1[ptr1:]
                break
            elif i % 2 == 0:
                res += word1[ptr1]
                ptr1 += 1
            elif i % 2 != 0:
                res += word2[ptr2]
                ptr2 += 1
            i += 1
        return res