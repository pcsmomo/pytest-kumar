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

### 10. Running Our Tests

```sh
poetry add pytest-watcher
ptw .
ptw -v .
```

### 12. Understanding Test Outputs(2/2)

[`.pytest_cache` explanation](https://docs.pytest.org/en/7.4.x/how-to/cache.html)

```sh
pytest --lf -x .  # stopping after 1 failures
ptw --lf -x .

# stepwise
pytest --lf --sw .
ptw --lf --stepwise .
```

### A. Assignment 1 question

> [Vscode markdown pasting image as default](https://dev.to/francecil/vscode-new-version-179-supports-pasting-images-in-markdown-1fd2)\
> `{ "markdown.editor.filePaste.enabled": false }`

```sh
pytest .
pytest -s . # displaying print()

pytest -h | less # help, there are a bunch of options
```

## Section 4: Pytest: Assertions and Test Discovery

### 15. Test Class

```sh
poetry shell
python
>>> help(str)
# Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
```

```sh
>>> import math
>>> help(math)
>>> help(math.sqrt)
```

### 16. Test Discovery

```sh
# ./01-pytest-101

# run directory
pytest -v .
pytest -v py_assertions

# run test file
pytest -v py_assertions/test_module01.py

# run test class
pytest -v py_assertions/test_module02.py::TestMyStuff

# run test module
pytest -v py_assertions/test_module01.py::test_a1
pytest -v py_assertions/test_module02.py::TestMyStuff::test_type
```

</details>
