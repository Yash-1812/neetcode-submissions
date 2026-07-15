class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s = str1 if len(str1) < len(str2) else str2
        other = str2 if s == str1 else str1
        i = 0
        div = ''
        res = ''
        while i < len(s):
            div += s[i]
            len_div = len(div)
            check = True
            for j in range(0 , len(other) , len_div):
                word = other[j : j + len_div]
                if word != div:
                    check = False
                    break
            if check and len(s) % len_div == 0:
                if len(div) > len(res):
                    res = div
            i += 1
        return res