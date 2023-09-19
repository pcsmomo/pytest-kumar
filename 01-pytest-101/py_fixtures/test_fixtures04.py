import pytest

months = ["Jan", "Feb", "Mar"]


def test_checkrequest(setup04):
    print()
    print(setup04)
    assert "April" in setup04
    assert len(setup04) == 4
