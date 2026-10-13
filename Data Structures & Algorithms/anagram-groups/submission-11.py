class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = collections.defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            words[tuple(freq)].append(s)
        res = []
        for word in words:
            temp = list(words[word])
            res.append(temp)
        return res

        