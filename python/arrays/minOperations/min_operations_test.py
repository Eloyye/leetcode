from python.arrays.minOperations import minOperations


def test_13_17():
    nums = [13, 7, 13, 7, 13, 7, 13, 13, 7]
    assert minOperations(nums) == 4


def test_1():
    nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]
    assert minOperations(nums) == 4


def test_2():
    nums = [2, 1, 2, 2, 3, 3]
    assert minOperations(nums) == -1

    def test_3(self):
        nums = [3, 3]
        assert minOperations(nums) == 1
