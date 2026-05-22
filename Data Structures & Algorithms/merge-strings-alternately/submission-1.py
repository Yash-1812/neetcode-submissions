class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        j = 0
        c = 0
        output_str = ""

        while c < (len(word1) + len(word2)):
            
            if i == len(word1):
                output_str += word2[j : len(word2) + 1]
                break
            if j == len(word2):
                output_str += word1[i : len(word1) + 1]
                break

            if c % 2 == 0:
                output_str += word1[i]
                i += 1
            if c % 2 == 1:
                output_str += word2[j]
                j += 1

            c += 1

        return output_str