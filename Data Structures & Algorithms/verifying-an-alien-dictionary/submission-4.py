class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        idx_order = collections.defaultdict(int)
        for i , ch in enumerate(order):
            idx_order[ch] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            ptr1 , ptr2 = 0 , 0
            while ptr1 < len(word1):
                if ptr1 == len(word2):
                    return False
                if idx_order[word2[ptr2]] < idx_order[word1[ptr1]]:
                    return False
                if idx_order[word2[ptr2]] > idx_order[word1[ptr1]]:
                    break
                ptr1 += 1
                ptr2 += 1
        return True