class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        w1 , w2 = strs[0] , strs[1]
        ptr1 , ptr2 = 0 , 0
        prefix = ""
        while ptr1 < len(w1) and ptr2 < len(w2) and w1[ptr1] == w2[ptr2]:
            prefix += w1[ptr1]
            ptr1 += 1
            ptr2 += 1
        if len(strs) == 2:
            return prefix
        for i in range(2 , len(strs)):
            w = strs[i]
            for j in range(len(prefix)):
                if j == len(w):
                    prefix = w
                    break
                if w[j] != prefix[j]:
                    prefix = w[0 : j]
                    break
        return prefix