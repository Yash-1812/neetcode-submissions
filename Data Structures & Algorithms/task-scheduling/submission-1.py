class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1
        max_freq = max(freq)
        k = 0
        for i in range(26):
            if freq[i] == max_freq:
                k += 1
        return max(len(tasks) , ((max_freq - 1) * (n + 1) + k))