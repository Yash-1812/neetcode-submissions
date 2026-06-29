class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        output = []
        for start , end in queries:
            count = 0
            for i in range(start , end + 1):
                s = words[i]
                n = len(s) - 1
                if ((s[0] == 'a' or s[0] == 'e' or s[0] == 'i' or s[0] == 'o' or s[0] == 'u') and (s[n] == 'a' or s[n] == 'e' or s[n] == 'i' or s[n] == 'o' or s[n] == 'u')):
                   count += 1
            output.append(count)
        return output
