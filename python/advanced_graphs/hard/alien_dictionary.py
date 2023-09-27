from enum import Enum
from typing import List


class PathState(Enum):
    VISITED = 0
    CURRENT_PATH = 1
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        n = len(words)
        def construct_adjacency_list(words: List[str]) -> (dict[str : set[str]], bool):
            nonlocal n
            adj = { character : set() for word in words for character in word }
            for i in range(n - 1):
                word1, word2 = words[i], words[i + 1]
                word1_length = len(word1)
                word2_length = len(word2)
                min_len = min(word1_length, word2_length)
                if word1_length > word2_length and word1[:min_len] == word2[: min_len]:
                    return {}, True
                for j in range(min_len):
                    word1_char = word1[j]
                    word2_char = word2[j]
                    if word1_char != word2_char:
                        adj[word1_char].add(word2_char)
            return adj, False
        adjacency_list, err = construct_adjacency_list(words)
        if err:
            return ""
        visited = {}
        res = []
        def dfs(char : str) -> PathState:
            if char in visited:
                return visited[char]
            visited[char] = PathState.CURRENT_PATH
            for neighbor_character in adjacency_list[char]:
                if dfs(neighbor_character) == PathState.CURRENT_PATH:
                    return PathState.CURRENT_PATH
            visited[char] = PathState.VISITED
            res.append(char) # post order dfs, this is the crux of topological sort
            return PathState.VISITED
        for character in adjacency_list:
            has_cycle = dfs(character) == PathState.CURRENT_PATH
            if has_cycle:
                return ""
        res.reverse()
        return "".join(res)