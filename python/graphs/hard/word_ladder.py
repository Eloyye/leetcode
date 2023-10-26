from collections import defaultdict, deque
from typing import List

def ladderLength2(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    wordList.append(beginWord)
    pattern_adj_list = construct_adj_list(wordList)
    return bfs(beginWord, endWord, pattern_adj_list)

def construct_adj_list(wordList):
    neighbors = defaultdict(list)
    for word in wordList:
        for j in range(len(word)):
            pattern = get_pattern(j, word)
            neighbors[pattern].append(word)
    return neighbors


def bfs(beginWord, endWord, neighbors):
    # contains visit set
    # contains deque/priority queue that is able to pop FIFO
    visit = set([beginWord])
    q = deque([beginWord]) # all the values inside queue have been visited
    length_result = 1
    while q:
        for _ in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return length_result
            for j in range(len(word)):
                pattern = get_pattern(j, word)
                for neighbor_word in neighbors[pattern]:
                    if neighbor_word not in visit:
                        visit.add(neighbor_word)
                        q.append(neighbor_word)
        length_result += 1
    return 0


def get_pattern(j, word):
    return word[:j] + '*' + word[j + 1:]


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    neighbors = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            neighbors[pattern].append(word)
    visit = set([beginWord])
    q = deque([beginWord])
    length_result = 1
    while q:
        for i in range(len(q)):
            word = q.popLeft()
            if word == endWord:
                return length_result
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neighbor_word in neighbors[pattern]:
                    if neighbor_word not in visit:
                        visit.add(neighbor_word)
                        q.append(neighbor_word)
        length_result += 1
    return 0