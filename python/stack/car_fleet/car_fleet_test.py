from python.stack.car_fleet.car_fleet import car_fleet


def test1():
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3

def test2():
    assert car_fleet(10, [3], [3]) == 1

def test3():
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1
