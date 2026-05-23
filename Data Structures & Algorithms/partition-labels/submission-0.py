class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_seen = {char : i for i, char in enumerate(s)}
        result = []
        start = 0
        end = 0

        for i , char in enumerate(s):
            end = max(end , last_seen[char])

            if i == end:
                substring_length = end - start + 1
                result.append(substring_length)
                start = i + 1
        
        return result