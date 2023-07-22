from collections import defaultdict
from typing import List


# O(mn log n ) solution
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Create a default dictionary with a list as the default value type
    anagram_dict = defaultdict(list)

    # Iterate over the input strings
    for word in strs:
        # Sort the string and use it as a key (since anagrams will become equal when sorted)
        sorted_word_tuple = tuple(sorted(word))
        # Add the original word to the list of anagrams of the sorted word
        anagram_dict[sorted_word_tuple].append(word)

    # Return the groups of anagrams as a list of lists
    return list(anagram_dict.values())

def efficientGroupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list) # mapping charCount to list of Anagrams

    # s is string mapping to some anagrams
    for s in strs:
        #frequency count of each character
        count = [0] * 26 # a ... z

        #iterate through every character in s
        for c in s:
            #ascii order
            # ord(c) - ord("a") maps a to 0 and z to 25; this "interpolates"
            count[ord(c) - ord("a")] += 1
            # keys cannot be list, but tuples can
        res[tuple(count)].append(s)
    return res.values()
