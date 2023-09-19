const = 9 / 5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


# print(cent_to_fah())


def test_case01():
    assert type(const) == float


def test_case02():
    assert cent_to_fah(0) == 32


def test_case03():
    assert cent_to_fah(38) == 100.4
