class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen_queue = []
        for i in range(len(s)):
            while s[i] in seen_queue:
                seen_queue.pop(0)
            seen_queue.append(s[i])
            max_len = max(max_len , len(seen_queue))
        return max_len

