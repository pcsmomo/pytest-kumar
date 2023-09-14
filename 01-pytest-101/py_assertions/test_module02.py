class TestMyStuff:
    def test_type(self):
        assert type(1) == int
        assert type(1.0) == float
        assert type("1") == str
        assert type([1]) == list
        assert type((1,)) == tuple
        assert type({1}) == set
        assert type({1: 1}) == dict
        assert type(None) == type(None)

    def test_strs(self):
        assert str.upper("python") == "PYTHON"
        assert "pytest".capitalize() == "Pytest"
