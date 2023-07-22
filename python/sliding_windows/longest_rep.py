from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # store the frequency of each character
        freq = defaultdict(int)

        # initialize max_freq which stores the character with maximum frequency in the window
        max_freq = 0
        start = 0
        max_length = 0

        for end in range(len(s)):
            # increase the frequency of current character
            freq[s[end]] += 1

            # update max frequency character
            max_freq = max(max_freq, freq[s[end]])

            # if the current window size is greater than max_freq + k, then reduce the window size
            if (end - start + 1) > (max_freq + k):
                # decrease the frequency of character going out of window
                freq[s[start]] -= 1
                # move the window
                start += 1

            # update max length
            max_length = max(max_length, end - start + 1)

        return max_length

    # O(n) time and *O(1) space complexity because the range of keys is the length of the alphabet
    def characterReplacement2(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = max_len = start = 0
        for end, c in enumerate(s):
            #update frequency
            freq[c] += 1
            max_freq = max(max_freq, freq[c])
            # max_freq + k is so far the longest possible
            if (end - start + 1) > (max_freq + k):
                freq[s[start]] -= 1
                start += 1
            #update max_len
            max_len = max(max_len, end - start + 1)
        return max_len