class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLastLetterOfWord = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str):
        head = self.root
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode()
            head = head.children[c]
        head.isLastLetterOfWord = True
    def search(self, word : str) -> bool:
        def explore(startingIndex : int, rootNode : TrieNode):
            head = rootNode
            for i in range(startingIndex, len(word)):
                currentCharacter = word[i]
                if currentCharacter == ".":
                    for childrenNode in head.children.values():
                        if explore(startingIndex + 1, childrenNode):
                            return True
                    return False
                else:
                    if currentCharacter not in head.children:
                        return False
                    head = head.children[currentCharacter]
            return head.isLastLetterOfWord
        return explore(0, self.root)