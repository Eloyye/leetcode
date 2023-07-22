from collections import defaultdict, deque
from typing import List

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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