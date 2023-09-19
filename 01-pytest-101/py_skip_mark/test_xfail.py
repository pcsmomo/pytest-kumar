import pytest
import sys


def test_strjoin():
    s1 = "Python,Pytest and Automation"
    l1 = ["Python,Pytest", "and", "Automation"]
    l2 = ["Python", "Pytest and Automation"]
    assert " ".join(l1) == s1


@pytest.mark.xfail(raises=IndexError, reason="known issue")
# @pytest.mark.xfail(raises=TypeError, reason="known issue")
def test_str04():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[100]


# xfail, it supposed to fail
@pytest.mark.xfail(sys.platform == "darwin", reason="works only on mac darwin")
def test_str05():
    letters = "abcd"
    num = 1234
    assert letters + num == "abcd1234"


# XPASS
@pytest.mark.xfail(reason="known issue")
def test_str06():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[10]
