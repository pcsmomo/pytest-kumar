from pytest_bdd import scenario, scenarios, given, when, then, parsers
from pathlib import Path
import pytest

featureFileDir = "myfeatures"
featureFile = "parameterize.feature"
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)


@given("there are 3 varieties of fruits", target_fixture="fruits")
def existing_fruits():
    fruits = {"apples", "grapes", "strawberrys"}
    return fruits


@when("we add a same variety of fruit")
def add_a_fruit(fruits):
    fruits.add("grapes")


@then("there is same count of varieties")
def same_count(fruits):
    assert len(fruits) == 3


@then("if we add a different variety of fruit")
def add_diff_variety(fruits):
    fruits.add("cherry")


@then(parsers.parse("the count of varieties increases to {count:d}"))
def count_increases(fruits, count):
    print(fruits)
    assert len(fruits) == count
