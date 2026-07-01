class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord , 1)])
        while queue:
            curr_word , level = queue.popleft()
            if curr_word == endWord:
                return level
            for i in range(len(curr_word)):
                original_char = curr_word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = curr_word[:i] + c + curr_word[i + 1:]
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word , level + 1))

        return 0