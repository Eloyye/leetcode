from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs : List[str]) -> str:
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, str : str) -> List[str]:
        # write your code here
        # i is the start position of a len + delimiter + string
        res, i = [], 0

        while i < len(str):
            # we want j to be the position of the delimiter
            j = i
            #we want to find a delimiter
            while str[j] != '#':
                # remember that 1234 could be the len of string
                j += 1
            #how much we need to read
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            #beginning of the first digit of next num
            i = j + 1 + length
        return res
