import unittest


def solution(x : str) -> str:
    n = len(x)
    res = []

    def get_inverted_char(char_to_append: str) -> str:
        end_char_ascii = ord('z')
        start_char_ascii = ord('a')
        inverted_char_ascii = (end_char_ascii - ord(char_to_append)) + start_char_ascii
        char_to_append = chr(inverted_char_ascii)
        return char_to_append

    for i in range(n):
        char_to_append = x[i]
        if char_to_append.isalnum() and char_to_append.islower():
            char_to_append = get_inverted_char(char_to_append)
        res.append(char_to_append)
    return "".join(res)

class TestCipher(unittest.TestCase):
    def test1(self):
        cipher = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
        result = solution(cipher)
        expected = "did you see last night's episode?"
        self.assertEqual(result, expected)
    def test2(self):
        cipher = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
        result = solution(cipher)
        expected = "Yeah! I can't believe Lance lost his job at the colony!!"
        self.assertEqual(result, expected)