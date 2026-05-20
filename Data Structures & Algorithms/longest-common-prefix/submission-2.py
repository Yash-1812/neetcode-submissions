class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for i in range(1 , len(strs)):
            if strs[i] == "":
                longest = strs[i]
                break
            for j in range(len(strs[i])):
                if j == len(longest):
                    break
                elif j == len(strs[i]) - 1:
                    longest = strs[i]
                    break

                elif longest[j] == strs[i][j]:
                    continue
                elif longest[j] != strs[i][j]:
                    longest = strs[i][:j]
                    break

        return longest

