from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for ch in s:
            freq1[ch] += 1
        for ch in t:
            freq2[ch] += 1
        for ch in freq1:
            if ch not in freq2 or freq1[ch] != freq2[ch]:
                return False
        for ch in freq2:
            if ch not in freq1 or freq1[ch] != freq2[ch]:
                return False
        return True