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


@pytest.fixture(scope="session")
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2
    print("\nFixture setup02 closing")


@pytest.fixture()
def setup04(request):
    print("\n in Fixture setup04")
    print("\n type of request" + str(type(request)))
    print(request)
    print("\n Fixture Scope: " + str(request.scope))
    print("\n Calling function: " + str(request.function.__name__))
    print("\n Calling module: " + str(request.module.__name__))

    print("*" * 50)
    mon = getattr(request.module, "months")
    mon.append("April")
    yield mon


@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == "list":
            return [1, 2, 3]
        elif name == "tuple":
            return (1, 3, 4)

    return get_structure
