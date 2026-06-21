class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {char : i for i , char in enumerate(s)}
        result = []
        start , end = 0 , 0
        for i , ch in enumerate(s):
            end = max(end , last_occurence[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result