from python.dp.medium.house_robber.house_robber import HouseRobberSolution


def test1():
    inp = [1, 2, 3, 1]
    out = 4
    rob = HouseRobberSolution().rob
    assert rob(inp) == out


def test2():
    inp = [2, 7, 9, 3, 1]
    out = 12
    rob = HouseRobberSolution().rob
    assert rob(inp) == out


def test3():
    inp = [2, 1, 1, 2]
    out = 4
    rob = HouseRobberSolution().rob
    assert rob(inp) == out
