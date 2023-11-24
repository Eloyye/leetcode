import unittest


class Solution:
    def unlocked_skins(self, current_level : int, skin_data : str) -> str:
        parsed_strings = [skin for skin in skin_data.split(',')]
        parsed_segments = [skin.split(':') for skin in parsed_strings]
        parsed_data = [skin_name for skin_name, required_level in parsed_segments if int(required_level) <= current_level]
        return ",".join(parsed_data)

class UnlockedSkinsTest(unittest.TestCase):
    def test1(self):
        unlocked_skins = Solution().unlocked_skins
        current_level = 10
        skin_data = "Spectral Guardian:5,Dark Matter Trooper:15,Cosmic Voyager:10,Neon Striker:20,Dragon Knight:8"
        expected = "Spectral Guardian,Cosmic Voyager,Dragon Knight"
        res = unlocked_skins(current_level, skin_data)
        print(res)
        self.assertEqual(expected, res)