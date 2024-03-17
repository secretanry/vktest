import pytest


# tuple tests
def test_tuple_creation():
    t = (1, {2: 3}, [4, 5, 6])
    assert isinstance(t, tuple)
    assert len(t) == 3
    assert t[0] == 1
    assert t[1] == {2: 3}
    assert t[2] == [4, 5, 6]


# negative test
def test_tuple_mutable():
    try:
        t1 = (2, 2, 2)
        t1[1] = 3
        assert False
    except TypeError:
        assert True


# parametrized test
@pytest.mark.parametrize("index, exp", [(0, 1), (1, 2), (2, 3)])
def test_tuple_indexing(index, exp):
    t = (1, 2, 3)
    assert t[index] == exp


# float test
def test_float_create():
    f = 5.00
    assert isinstance(f, float)
    assert f == 5.00


def test_float_multiply():
    result = 2.0 * 3.0
    assert isinstance(result, float)
    assert result == 6.0


def test_float_add():
    result = 2.0 + 3.0
    assert isinstance(result, float)
    assert result == 5.0
