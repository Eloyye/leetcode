import unittest
from collections import defaultdict, Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n, update_max = len(s), max
        freq = Counter()
        longest_len = left = max_char_freq = 0
        for right in range(n):
            right_window_character, left_window_character = s[right], s[left]
            freq[right_window_character] += 1
            max_char_freq = update_max(max_char_freq, freq[right_window_character])
            current_window_length, current_possible_valid_length = (right - left + 1), (max_char_freq + k)
            if current_window_length > current_possible_valid_length:
                freq[left_window_character] -= 1
                left += 1
                current_window_length -= 1
            longest_len = update_max(longest_len, current_window_length)
        return longest_len
    def character_replacement(self, s: str, k: int) -> int:
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

class LongestRepTests(unittest.TestCase):
    def test1(self):
        characterReplacement = Solution().characterReplacement
        s = "AABABBA"
        k = 1
        self.assertEquals(4, characterReplacement(s, k))