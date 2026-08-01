class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = collections.defaultdict(int)
        for i in range(len(s)):
            ch = s[i]
            last[ch] = i
        res = []
        farthest = 0
        start = 0
        for i in range(len(s)):
            farthest = max(farthest , last[s[i]])
            if i == farthest:
                res.append(i - start + 1)
                start = i + 1
        return res