from typing import List


def letterCombinations( digits: str) -> List[str]:
    mapping = {
       '2': ['a', 'b', 'c'],
       '3': ['d', 'e', 'f'],
       '4': ['g', 'h', 'i'],
       '5': ['j', 'k', 'l'],
       '6': ['m', 'n', 'o'],
       '7': ['p', 'q', 'r', 's'],
       '8': ['t', 'u', 'v'],
       '9': ['w', 'x', 'y', 'z'],
    }
    res = []

    def bt(i, subset):
        if i == len(digits):
            res.append("".join(subset))
            return
        l = mapping[digits[i]]
        for j in range(len(l)):
            # incude j
            subset.append(j)
            bt(i + 1, subset)
            subset.pop()
            # exclude j
            bt(i + 1, subset)

    bt(0, [])
    return res

letterCombinations("23")
