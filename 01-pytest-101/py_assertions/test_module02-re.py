# def test_type(self):
#         assert type(1) == int
#         assert type(1.0) == float
#         assert type("1") == str
#         assert type([1]) == list
#         assert type((1,)) == tuple
#         assert type({1}) == set
#         assert type({1: 1}) == dict
#         assert type(None) == type(None)


class TestReRunFailed:
    """
    https://docs.pytest.org/en/7.1.x/how-to/cache.html
    Run this test with the following command:
    $ pytest --lf -v test_module03.py
    $ pytest --ff -v test_module03.py
    $ pytest --lf --sw -vtest_module03.py
    """

    def test_type(self):
        assert type(1) == int
        # assert type(1) == str

    def test_type2(self):
        assert type(1.0) == float
        # assert type(1.0) == str

    def test_type3(self):
        assert type("1") == str

    def test_type4(self):
        assert type([1]) == list

    def test_type5(self):
        assert type((1,)) == tuple

    def test_type6(self):
        assert type({1}) == set

    def test_type7(self):
        assert type({1: 1}) == dict

    def test_type8(self):
        assert type(None) == type(None)

    def test_strs(self):
        assert str.upper("python") == "PYTHON"
        assert "pytest".capitalize() == "Pytest"
