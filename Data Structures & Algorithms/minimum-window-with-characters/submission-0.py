from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_map = Counter(t)
        min_len = float('inf')
        output = ""
        for i in range(len(s)):
            if s[i] in t:
                s_map = collections.defaultdict(int)
                sub = ""
                for j in range(i , len(s)):
                    if s_map == t_map:
                        if len(sub) < min_len:
                            min_len = len(sub)
                            output = sub
                        break
                    if s[j] not in t:
                        sub += s[j]
                        continue
                    if s[j] in s_map:
                        if s_map[s[j]] < t_map[s[j]]:
                            s_map[s[j]] += 1
                            sub += s[j]
                        else:
                            sub += s[j]
                        continue
                    sub += s[j]
                    s_map[s[j]] += 1
                if s_map == t_map:
                    if len(sub) < min_len:
                        min_len = len(sub)
                        output = sub
        return output if output else ""