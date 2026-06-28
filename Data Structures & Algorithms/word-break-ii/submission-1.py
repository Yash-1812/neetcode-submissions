class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        curr = []
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(curr))
            for j in range(i , len(s)):
                if s[i:j + 1] in wordDict:
                    curr.append(s[i:j+1])
                    backtrack(j + 1)
                    curr.pop()
        backtrack(0)
        return res