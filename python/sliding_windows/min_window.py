from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""

    # countT, window == countS
    countT, window = defaultdict(int), defaultdict(int)
    # Initialize the freq for t
    for c in t:
        countT[c] += 1

    # need : is the number of UNIQUE characters in t
    # have: the number of characters in s that match t in the window
    have, need = 0, len(countT)
    # res is a pair containing the left and right pointer of the window
    # here we initialize it to -1, -1, and the length if infinite for purpose of comparability
    res, resLen = [-1, -1], float("infinity")
    #left pointer
    l = 0
    #iterate through right pointer
    for r, c  in enumerate(s):
        #increment character frequency to window
        window[c] += 1

        # check if that current char matches in t and that the frequency is the same
        if c in countT and window[c] == countT[c]:
            have += 1

        #this means that the window contains all the chars in t
        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    # the left and the right pointers of the result
    l, r = res
    # return that substring as long as the answer substring exists
    return s[l: r + 1] if resLen != float("infinity") else ""

res = minWindow("abcadtria", "aa")
print(res)
