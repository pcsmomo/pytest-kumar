import pytest
import sys

const = 9 / 5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


# print(cent_to_fah())


@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01():
    assert type(const) == float


@pytest.mark.skipif(
    sys.version_info > (3, 8),
    reason="doesn't work on py version above 3.8",
    # sys.version_info > (3, 11, 4),
    # reason="Python version is greater than 3.11.4",
)
def test_case02():
    print(sys.version_info)
    assert cent_to_fah(0) == 32


def test_case03():
    assert cent_to_fah(38) == 100.4
