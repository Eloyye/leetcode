import unittest


class TrieNode:
    def __init__(self):
        self.childrenCharacters = [None] * 26
        self.isLastCharacterOfWord = False
class TrieNode2:
    def __init__(self):
        self.childrenCharacters = {}
        self.isLastCharacterOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        head = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not head.childrenCharacters[i]:
                head.childrenCharacters[i] = TrieNode()
            head = head.childrenCharacters[i]
        head.isLastCharacterOfWord = True

    def search(self, word: str) -> bool:
        # dummy -> a -> p -> p -> l -> e
        def dfs(word: str, starting_node: TrieNode):
            if not starting_node:
                return False
            if not word:
                return starting_node.isLastCharacterOfWord
            c = word[0]
            if c == '.':
                for i in range(len(starting_node.childrenCharacters)):
                    target_node = starting_node.childrenCharacters[i]
                    if target_node and dfs(word[1:], target_node):
                        return True
                return False
            else:
                i = ord(c) - ord('a')
                if not starting_node.childrenCharacters[i]:
                    return False
                return dfs(word[1:], starting_node.childrenCharacters[i])
        return dfs(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
class WordDictionaryTest(unittest.TestCase):
    def test1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        self.assertFalse(wordDictionary.search("pad"))
        self.assertTrue(wordDictionary.search("bad"))
        self.assertTrue(wordDictionary.search(".ad"))
        self.assertTrue(wordDictionary.search("b.."))
