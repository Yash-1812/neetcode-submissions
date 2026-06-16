from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        result = []
        for i in range(len(strs)):
            if strs[i] == 'A':
                continue
            c = Counter(strs[i])
            output = [strs[i]]
            for j in range(i + 1 , len(strs)):
                c2 = Counter(strs[j])
                if c == c2:
                    output.append(strs[j])
                    strs[j] = 'A'
            result.append(output.copy())
        return result