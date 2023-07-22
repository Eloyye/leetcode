import unittest


class TrieNode:
    def __init__(self, char : str):
        self.char = char
        self.nextLetters = {}
        self.isLastLetterOfWord = False
    def insert(self, char : str):
        if not self.nextLetters.get(char):
            self.nextLetters[char] = TrieNode(char)

    def getIsLastLetterOfWord(self):
        return self.isLastLetterOfWord

    def setIsLastLetterOfWord(self):
        self.isLastLetterOfWord = True

    def getCharacter(self) -> str:
        return self.char

    def getNextLetter(self, char : str):
        return self.nextLetters[char] if self.nextLetters.get(char) else None

class Trie:

    def __init__(self):
        self.dummyNode = TrieNode("%")
    def insert(self, word: str) -> None:
        head = self.dummyNode
        for c in word:
            head.insert(c)
            head = head.getNextLetter(c)
        head.setIsLastLetterOfWord()

    def search(self, word: str) -> bool:
        head = self.dummyNode
        for c in word:
            head = head.getNextLetter(c)
            if not head:
                return False
        return head.isLastLetterOfWord

    def startsWith(self, prefix: str) -> bool:
        head = self.dummyNode
        for c in prefix:
            head = head.getNextLetter(c)
            if not head:
                return False
        return True

class TrieTesting(unittest.TestCase):
    def test1(self):
        t = Trie()
        t.insert("apple")
        self.assertTrue( t.search("apple"))
        self.assertFalse(  t.search("app") )
        self.assertTrue(t.startsWith("app"))
        t.insert("app")
        self.assertTrue(t.search("app"))
    def test2(self):
        t = Trie()
        self.assertFalse(t.search("a"))
