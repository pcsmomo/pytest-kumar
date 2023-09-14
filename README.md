# Python Automation Testing With Pytest by Kumar S

Python Automation Testing With Pytest by Kumar S

## Folder structure

-

## Details

<details open>
  <summary>Click to Contract/Expend</summary>

## Section 3: Pytest 101: Create Project and First Test

### 5. About Pytest

[Pytest docs - v7.4](https://docs.pytest.org/en/7.4.x/)

### 6. Pycharm: Create project and VirtualEnv

```sh
mkdir 01-pytest-101
cd 01-pytest-101
poetry init
poetry install
```

### 7. Pycharm: Installing python packages

```sh
poetry add pytest
poetry add requests

pip list # or pip3 list

# to share my dependencies
pip freeze > requirements.txt
pip install -r requirements.txt
```

### 9. Write First Tests & Tests Conventions

[pytest assert](https://docs.pytest.org/en/7.4.x/how-to/assert.html)

```sh
# ./01-pytest-101
pytest pytest_topics
pytest -v pytest_topics
```

#### Rules

- Name all the test modules with `test_<somename>.py`
- Name all the test function with `test_<somename>`
- Test classes should be named `Test<somename>.py`
- Properly group all the tests into test classes/packages

</details>
