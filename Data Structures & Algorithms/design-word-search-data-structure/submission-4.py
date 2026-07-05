class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(idx , root):
            curr = root
            for i in range(idx , len(word)):
                ch = word[i]
                if ch == '.':
                    for child in curr.children.values():
                        if dfs(i + 1 , child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.is_end_of_word
        return dfs(0 , self.root)
                    
