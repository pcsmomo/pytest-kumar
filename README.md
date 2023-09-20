# Python Automation Testing With Pytest by Kumar S

Python Automation Testing With Pytest by Kumar S

## Folder structure

- Section 3: Pytest 101: Create Project and First Test
  - `01-pytest-101/pytest_topics`
- Section 4: Pytest: Assertions and Test Discovery
  - `01-pytest-101/py_assertions`
- Section 5: Pytest: Skip/Mark and Pytest Options
  - `01-pytest-101/py_skip_mark`
- Section 6: Pytest: Parameterize and Setup/TearDown Tests(Fixtures)
  - `01-pytest-101/py_fixture_parameterize`

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

### 17. About `__init__.py`

we have two `test_module01.py` files under `pytest_topics` and `py_assertions`

if we delete both `__init__.py` files, we recives an error message when `pytest`

```sh
================================================================= ERRORS ==================================================================
_____________________________________________ ERROR collecting pytest_topics/test_module01.py _____________________________________________
import file mismatch:
imported module 'test_module01' has this __file__ attribute:
  /Users/noah/Documents/study/study_codes/udemy/pytest-kumar/pytest-kumar-git/01-pytest-101/py_assertions/test_module01.py
which is not the same as the test file we want to collect:
  /Users/noah/Documents/study/study_codes/udemy/pytest-kumar/pytest-kumar-git/01-pytest-101/pytest_topics/test_module01.py
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
```

### 22. Skipping Tests

```sh
ptw -sv .
```

```sh
poetry shell
python
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_getquickenedcount', '_git', '_home', '_stdlib_dir', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']


>>> import pytest
>>> dir(pytest)
['Cache', 'CallInfo', 'CaptureFixture', 'Class', 'CollectReport', 'Collector', 'Config', 'DoctestItem', 'ExceptionInfo', 'ExitCode', 'File', 'FixtureLookupError', 'FixtureRequest', 'Function', 'HookRecorder', 'Item', 'LineMatcher', 'LogCaptureFixture', 'Mark', 'MarkDecorator', 'MarkGenerator', 'Metafunc', 'Module', 'MonkeyPatch', 'OptionGroup', 'Package', 'Parser', 'PytestAssertRewriteWarning', 'PytestCacheWarning', 'PytestCollectionWarning', 'PytestConfigWarning', 'PytestDeprecationWarning', 'PytestExperimentalApiWarning', 'PytestPluginManager', 'PytestRemovedIn8Warning', 'PytestReturnNotNoneWarning', 'PytestUnhandledCoroutineWarning', 'PytestUnhandledThreadExceptionWarning', 'PytestUnknownMarkWarning', 'PytestUnraisableExceptionWarning', 'PytestWarning', 'Pytester', 'RecordedHookCall', 'RunResult', 'Session', 'Stash', 'StashKey', 'TempPathFactory', 'TempdirFactory', 'TestReport', 'TestShortLogReport', 'Testdir', 'UsageError', 'WarningsRecorder', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__getattr__', '__loader__', '__name__', '__package__', '__path__', '__pytestPDB', '__spec__', '__version__', 'approx', 'cmdline', 'console_main', 'deprecated_call', 'exit', 'fail', 'fixture', 'freeze_includes', 'hookimpl', 'hookspec', 'importorskip', 'main', 'mark', 'param', 'raises', 'register_assert_rewrite', 'set_trace', 'skip', 'version_tuple', 'warns', 'xfail', 'yield_fixture']
>>> print(pytest.__version__)
7.4.2
```

### 23. Grouping/Marking Tests(1/3)

```sh
pytest -m <markername>


# py_skip_mark/test_markers.py
ptw -vs . -m sanity
pytest -vs -m sanity


# test_markers.py:4
#   /Users/noah/Documents/study/study_codes/udemy/pytest-kumar/pytest-kumar-git/01-pytest-101/py_skip_mark/test_markers.py:4: PytestUnknownMarkWarning: Unknown pytest.mark.sanity - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.sanity

# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
```

[pytest - registering marks](https://docs.pytest.org/en/stable/how-to/mark.html#registering-marks)

### 24. Marking Tests(2/3)

### mark list

- sanity
- str

```sh
ptw -vs . -m "not sanity"
ptw -vs . -m "sanity and not str"
ptw -vs . -m "sanity and str"
ptw -vs . -m "sanity or str"
```

### 25. Marking Tests(3/3)

```py
# mark for whole module or class
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]
```

### 26. xfail: Expecting to Fail Marker(1/2)

[pytest xfail - assumtion to fail][https://docs.pytest.org/en/7.1.x/how-to/skipping.html#xfail-mark-test-functions-as-expected-to-fail]

similar to raising exception in the test, but `xfail` shows the better labels such as `XFAIL` or `XPASS`

```sh
# 01-pytest-101/py_skip_mark

ptw -vs .

# test_xfail.py::test_str04 XPASS (known issue)
# test_xfail.py::test_str05 XFAIL
```

### 28. Run test by testname (both filename or module name)

```sh
pytest -k <substring of the file/module name>

# 01-pytest-101/
pytest -v -k "module"

# --tb : Traceback print mode (auto/long/short/line/native/no)
pytest -v -k "module" --tb=no

pytest -v -k "str or case" --tb=no
pytest -v -k "case or xfail" --tb=no
pytest -v -k "module and not case" --tb=no
```

### 29. Pytest Cmd line options(1/2)

```sh
pytest --showlocals # show local variables in tracebacks
pytest -l           # show local variables (shortcut)

pytest --tb=auto    # (default) 'long' tracebacks for the first and last entry,
                    # but 'short' style for the other entries
pytest --tb==long   # exhaustive, informative traceback formatting
pytest --tb==short  # shorter traceback format
pytest --tb==line   # only one line per failure
pytest --tb==native # Python standard library formatting
pytest --tb==no     # no traceback at all
```

#### exit on failure

```sh
pytest -x   # exit on the first failure
pytest --maxfail=2

pytest -q
```

#### display modules, classes and functions

```sh
pytest --collect-only
```

#### if you want to change the testing order

[pypi pytest-order : a pytest plugin to order test execution](https://pypi.org/project/pytest-order/)

### 30. Pytest Cmd line options(2/2)

```sh
pytest --lf  # test only previously failed tests
pytest --ff
```

```sh
pytest --help


# we can see ini options here as well

# [pytest] ini-options in the first pytest.ini|tox.ini|setup.cfg|pyproject.toml file found:

#   markers (linelist):   Markers for test functions
#   empty_parameter_set_mark (string):
#                         Default marker for empty parametersets
#   norecursedirs (args): Directory patterns to avoid for recursion
#   testpaths (args):     Directories to search for tests when no files or directories are given on the command line
#   filterwarnings (linelist):
#                         Each line specifies a pattern for warnings.filterwarnings. Processed after -W/--pythonwarnings.
```

### 31. Test Outcomes

- PASSED (.): The test ran successfully.
- FAILED (F): The test did not run successfully (or XPASS + strict).
- SKIPPED (s): The test was skipped. You can tell pytest to skip a test by using either the @pytest.mark.skip() or pytest.mark.skipif() decorators, discussed in Skipping Tests .
- xfail (x): The test was expected to fail, so ran and failed. You can tell pytest that a test is expected to fail by using the @pytest.mark.xfail() decorator.
- XPASS (X): The test was not supposed to pass but ran and passed.
- ERROR (E): An exception happened outside of the test function, in either a fixture.

## Section 6: Pytest: Parameterize and Setup/TearDown Tests(Fixtures)

### 36. Fixture Basics(1/3)

- Fixture: functions that are run by pytest before (and sometimes after) the actual test functions.
  - Eg. setup DB connection, or initialize webdriver
- Can put fixtures in individual test files, or, in `conftest.py` for making fixtures available in multiple test files

### 38. Fixture Basics(3/3)

#### two ways to use fixtures

```py
@pytest.fixture()
def setup_list():
    print("\n in fixtures.. setup_list.. \n")
    city = ["New York", "London", "Riyadh", "Singapore", "Mumbai"]
    return city

# way 1
def test_getItem(setup_list):
  assert setup_list[0] == "New York


# way 2
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo02():
  assert 1 == 1
```

### 41. Sharing Fixtures

#### `conftest.py`

- Share fixtures across multiple tests.
- Can have single `conftest.py` in centralized directory for all test to access the fixtures.
- Also, can have other `conftest.py` files in subdirectories.
- It should not be imported by test files.

> fixtures can be overriden from test module level

### 42. Tracing Fixture Execution

```sh
pytest -vs -k test_fixtures03
pytest -v -k test_fixtures03
```

```sh
pytest -vs -k test_fixtures03 --setup-show

# the scope of setup01 is set to `module`
test_fixtures03.py::test_delItem
    SETUP    M setup01
        py_fixtures/test_fixtures03.py::test_delItem (fixtures used: setup01)['mon', 'tue', 'wed']
PASSED
test_fixtures03.py::test_removeItem
        SETUP    F setup02
        py_fixtures/test_fixtures03.py::test_removeItem (fixtures used: setup02)['thur', 'fri', 'sat', 'sun']
PASSED
Fixture setup02 closing

        TEARDOWN F setup02
Fixture setup02 closing

    TEARDOWN M setup01
```

```sh
pytest -vs -k test_fixtures03 --setup-show

# the scope of setup01 is set to default `function`
test_fixtures03.py::test_delItem
        SETUP    F setup01
        py_fixtures/test_fixtures03.py::test_delItem (fixtures used: setup01)['mon', 'tue', 'wed']
PASSED
Fixture setup02 closing

        TEARDOWN F setup01
test_fixtures03.py::test_removeItem
        SETUP    F setup02
        py_fixtures/test_fixtures03.py::test_removeItem (fixtures used: setup02)['thur', 'fri', 'sat', 'sun']
PASSED
Fixture setup02 closing

        TEARDOWN F setup02
```

- M: module
- F: function

### 45. Parametrizing from Fixtures(1/2)

```py
# name the test name using `ids`
@pytest.fixture(params=[(3, 4), [3, 5]], ids=["tuple", "list"])
def fixture01(request):
    return request.param
```

</details>
