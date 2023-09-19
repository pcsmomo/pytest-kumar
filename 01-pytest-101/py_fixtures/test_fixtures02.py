import pytest


weekdays1 = ["mon", "tue", "wed"]
weekdays2 = ["fri", "sat", "sun"]


@pytest.fixture()
def setup01():
    weekdays1.append("thur")
    yield weekdays1
    print("\n After yield in setup01 fixture")
    weekdays1.pop()


@pytest.fixture()
def setup02():
    weekdays2.insert(0, "thur")
    yield weekdays2


def test_extendList(setup01):
    print()
    print("weekdays1: ", weekdays1)
    print("weekdays2: ", weekdays2)
    print("setup01: ", setup01)
    setup01.extend(weekdays2)
    assert setup01 == ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]


def test_len(setup01, setup02):
    # eventually weekday1 and setup01 is the same object
    # and setup02 and weekdays2 are the same
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)
