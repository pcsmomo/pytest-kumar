def test_strjoin():
    s1 = "Python,Pytest and Automation"
    l1 = ["Python,Pytest", "and", "Automation"]
    l2 = ["Python", "Pytest and Automation"]
    assert " ".join(l1) == s1


def test_str04():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[10]


def test_str05():
    letters = "abcd"
    num = 1234
    assert letters + num == "abcd1234"
