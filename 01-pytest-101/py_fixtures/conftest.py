import pytest


def pytest_configure():
    pytest.weekdays1 = ["mon", "tue", "wed"]
    pytest.weekdays2 = ["fri", "sat", "sun"]


@pytest.fixture(scope="module")
def setup01():
    wk = pytest.weekdays1.copy()
    wk.append("thur")
    yield wk
    print("\n Fixture setup01 closing \n")


def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2
    print("\n Fixture setup02 closing \n")
