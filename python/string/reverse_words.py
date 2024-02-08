class Solution:
    def reverseWords(self, s: str) -> str:
        def split(words: str) -:
            word = []
            res = []
            for c in words:
                if c == ' ':
                    new_word = "".join(word)
                    res.append(new_word)
                    word = []
                else:
                    word.append(c)
            return res
        res = s.split()
        res.reverse()
        return "".join(res)
