from typing import List


class TrieNode:
    def __init__(self):
        self.children : dict[str, TrieNode] = {}
        self.isLastLetterOfWord = False
        self.refs = 0
    def addWord(self, word: str):
        head = self
        head.refs += 1
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode()
            head = head.children[c]
            head.refs += 1
        head.isLastLetterOfWord = True
    #optimization
    def removeWord(self, word : str):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rootTrie = TrieNode()
        for w in words:
            rootTrie.addWord(w)
        ROWS, COLS =  len(board), len(board[0]),
        result, visit = set(), set(),
        def dfs(r : int, c : int, rootNode : TrieNode, wordSoFar : str):
            #out of bounds
            # check if visited
            # check if word is in trie
            # check if the number of references is 0
            if r < 0 or c < 0 or r == ROWS or c == COLS \
                    or (r, c) in visit \
                    or board[r][c] not in rootNode.children \
                    or rootNode.children[board[r][c]].refs < 1:
                return
            visit.add((r, c))
            node = rootNode.children[board[r][c]]
            wordSoFar += board[r][c]
            if node.isLastLetterOfWord:
                node.isLastLetterOfWord = False
                result.add(wordSoFar)
                rootTrie.removeWord(wordSoFar)
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in direction:
                dfs(r + dr, c + dc, node, wordSoFar)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, rootTrie, "")
        return list(result)