import pytest


@pytest.fixture()
def setup_list():
    print("\n in fixtures.. setup_list.. \n")
    city = ["New York", "London", "Riyadh", "Singapore", "Mumbai"]
    return city
