class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        start = 0
        l1 = len(s1)
        for i in range(len(s2)):
            if s2[i] not in s1:
                start = i + 1
                continue
            while i - start + 1 > l1:
                start += 1
            if i - start + 1 == l1 and Counter(s2[start:i+1]) == c1:
                return True
        return False