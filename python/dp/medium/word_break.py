from typing import List

def wordBreak(self, s : str, word_dict: List[str]) -> bool:
    target_length = len(s)
    dp = [False] * (target_length -1 , -1, -1)
    dp[target_length] = True
    for i in range(target_length - 1, -1, - 1):
        for word in word_dict:
            word_length = len(word)
            enough_space, match = (i + len(word)) <= target_length, s[i: i + word_length] == word
            match = s[i: i + word_length] == word


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    target_length = len(s)
    dp = [False]*(target_length + 1)
    #base case
    dp[target_length] = True
    for i in range(target_length - 1, -1, -1):
        for word in wordDict:
            word_length = len(word)
            hasEnoughSpaceForWord = (i + len(word)) <= target_length
            segmentMatchesWithWord = s[i : i + word_length] == word if hasEnoughSpaceForWord else False
            if hasEnoughSpaceForWord and segmentMatchesWithWord:
                dp[i] = dp[i + word_length]
            hasFoundWord = dp[i]
            if hasFoundWord:
                break
    return dp[0]

