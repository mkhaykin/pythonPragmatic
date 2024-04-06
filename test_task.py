from main import task


def test():
    assert task([0], 0) == {'0'}

    assert task([0], 1) == set()

    assert task([1, 1], 2) == {'1+1'}

    assert task([1, 0], 1) == {'1+0', '1-0'}


def test1():
    assert task([1, 0], 10) == {'10'}


def test2():
    assert task([1, 1], 11) == {'11'}


def test3():
    assert task([2, 1], 21) == {'21'}


def test4():
    assert task([2, 1, 0], -8) == {'2-10'}


def test5():
    assert task([3, 2, 1], 321) == {'321'}


def test6():
    assert task([3, 2, 1], 99) == set()
