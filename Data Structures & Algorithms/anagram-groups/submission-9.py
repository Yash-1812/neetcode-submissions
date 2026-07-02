class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            words[tuple(count)].append(word)
        return list(words.values())