class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLastCharOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str):
        head = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not head.children[i]:
                head.children[i] = TrieNode()
            head = head.children[i]
        head.isLastCharOfWord = True
    def search(self, word: str) -> bool:
        head = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not head.children[i]:
                return False
            head = head.children[i]
        return head.isLastCharOfWord
    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not head.children[i]:
                return False
            head = head.children[i]
        return True
