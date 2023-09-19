import pytest


def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0

    with pytest.raises(Exception):
        assert 3 > 3


def func1():
    raise ValueError("Exception func1 raised")


def test_case02():
    with pytest.raises(Exception) as excinfo:
        assert (1, 2, 3) == (1, 2, 4)
    print(str(excinfo))  # run it with `-s` flag

    with pytest.raises(Exception) as excinfo2:
        func1()
    print(str(excinfo2))  # run it with `-s` flag
    assert str(excinfo2.value) == "Exception func1 raised"
