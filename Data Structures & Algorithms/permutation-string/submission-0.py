from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_map = Counter(s1)

        def isSame(s1_map , c):
            for ch in s1_map:
                if ch not in c or s1_map[ch] != c[ch]:
                    return False
            return True

        for i in range(n - 1 , len(s2)):
            sub = s2[i-n+1:i+1]
            c = Counter(sub)
            if isSame(s1_map , c):
                return True
        return False
