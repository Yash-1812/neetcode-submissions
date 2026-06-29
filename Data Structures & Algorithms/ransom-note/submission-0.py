class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for letter in r:
            if letter not in m:
                return False
            if r[letter] > m[letter]:
                return False
        return True