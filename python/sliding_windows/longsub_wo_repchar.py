# O(n) time , O(n) space
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = l = 0
    for r, c in enumerate(s):
        if c in used and l <= used[c]:
            l = used[c] + 1
        else:
            max_length = max(max_length, r - l + 1)
        used[c] = r
    return max_length

def lengthOfLongestSubstringSolution2(s: str) -> int:
    used = {} # keep track of characters and their indices {char : index}
    max_length = left = 0 #start, thinking of it as a left pointer
    for right, c in enumerate(s):
        if c in used and left <= used[c]:
            #moving the left pointer by 1
            left = used[c] + 1
        else:
            # not in used means that we increase the sliding window and thus increasing subsequence
            # account for 0-index
            max_length = max(max_length, right - left + 1)
        # keep track of the index to later check whether or not the used characters within the subarray
        used[c] = right
    return max_length

res = lengthOfLongestSubstring("abcabcbb")
print(res)

