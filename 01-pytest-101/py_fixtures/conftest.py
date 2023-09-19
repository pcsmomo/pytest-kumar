import pytest


def pytest_configure():
    pytest.weekdays1 = ["mon", "tue", "wed"]
    pytest.weekdays2 = ["fri", "sat", "sun"]


@pytest.fixture(scope="module")
def setup01():
    wk = pytest.weekdays1.copy()
    wk.append("thur")
    yield wk
    print("\nFixture setup02 closing")


@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2
    print("\nFixture setup02 closing")
