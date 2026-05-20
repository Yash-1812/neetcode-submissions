class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for ch1 , ch2 in zip(s , t):
            d1[ch1] = 1 + d1.get(ch1 , 0)
            d2[ch2] = 1 + d2.get(ch2 , 0)

        return d1 == d2