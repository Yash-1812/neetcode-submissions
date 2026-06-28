class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        test = Counter(s1)
        l1 = len(s1)
        l2 = len(s2)
        i = 0
        while i + l1 <= l2:
            substring = s2[i:i+l1]
            c = Counter(substring)
            if c == test:
                return True
            i += 1
        return False