import unittest


class TrieNode:
    def __init__(self):
        self.childrenCharacters = [None] * 26
        self.isLastCharacterOfWord = False
class TrieNode2:
    def __init__(self, c : str = None):
        self.chars = {}
        self.last = False
        self.c = c
class WordDictionary2:
    def __init__(self):
        self.root = TrieNode2()
    def addWord(self, word: str):
        head = self.root
        for c in word:
            if c not in head.chars:
                head.chars[c] = TrieNode2(c)
            head = head.chars[c]
        head.last = True
    def search(self, word : str):
        def dfs(word : str, node : TrieNode2) -> bool:
            if not node:
                return False
            if not word:
                return node.last
            c = word[0]
            if c == '.':
                for nei_node in node.chars.values():
                    if dfs(word[1:], nei_node):
                        return True
                return False
            else:
                if c not in node.chars:
                    return False
                return dfs(word[1:], node.chars[c])
        return dfs(word, self.root)
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
def exec_instr(top_ref, instr, values, expected):
    assert len(instr) == len(values)
    top_wd = None
    for i in range(len(instr)):
        cur_instr, cur_val, expected_res = instr[i], values[i][0] if values[i] else None, expected[i]
        if cur_instr == "WordDictionary":
            top_wd = WordDictionary2()
        elif top_wd and cur_instr == "search":
            r = top_wd.search(cur_val)
            top_ref.assertEqual(expected_res, r)
        elif top_wd and cur_instr == "addWord":
            top_wd.addWord(cur_val)
        else:
            raise Exception("Invalid input combination")
    return top_wd
class WordDictionaryTest(unittest.TestCase):
    def test1(self):
        wordDictionary = WordDictionary2()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        self.assertFalse(wordDictionary.search("pad"))
        self.assertTrue(wordDictionary.search("bad"))
        self.assertTrue(wordDictionary.search(".ad"))
        self.assertTrue(wordDictionary.search("b.."))
    def test2(self):
        instr = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
        values = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
        expected = [None,None,None,None,None,False,False,None,True,True,False,False,True,False]
        wd = exec_instr(self, instr, values, expected)

