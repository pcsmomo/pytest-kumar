import pytest
import sys

# it will apply to all tests in this module
pytestmark = pytest.mark.skipif(
    sys.platform in ["win32", "darwin"], reason="will run only on linux OS"
)
pytestmark = pytest.mark.skipif(
    sys.platform != "darwin", reason="will run only on mac darwin OS"
)

const = 9 / 5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


# print(cent_to_fah())


@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01():
    assert type(const) == float


# @pytest.mark.skipif(
#     sys.version_info > (3, 8),
#     reason="doesn't work on py version above 3.8",
#     # sys.version_info > (3, 11, 4),
#     # reason="Python version is greater than 3.11.4",
# )
@pytest.mark.skipif(cent_to_fah() == 32, reason="default value test, so skipping")
def test_case02():
    # print(sys.version_info)
    print(dir(sys))
    assert cent_to_fah(0) == 32


@pytest.mark.skipif(
    pytest.__version__ < "7.5.0", reason="pytest version is less then 7.5.0"
)
def test_case03():
    assert cent_to_fah(38) == 100.4
