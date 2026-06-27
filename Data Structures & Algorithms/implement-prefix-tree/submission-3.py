class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                temp.children[ch] = TrieNode()
                temp = temp.children[ch]
        temp.is_end_of_word = True

    def search(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        return temp.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        return True
        