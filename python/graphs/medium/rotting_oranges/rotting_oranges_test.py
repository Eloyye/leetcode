from python.graphs.medium.rotting_oranges.rotting_oranges import RottingOrangesSolution


def test1():
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    expected = 4
    oranges_rotting = RottingOrangesSolution().oranges_rotting
    assert oranges_rotting(grid) == expected


def test2():
    grid = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
    expected = -1
    oranges_rotting = RottingOrangesSolution().oranges_rotting
    assert oranges_rotting(grid) == expected