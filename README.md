# Python Automation Testing With Pytest by Kumar S

Python Automation Testing With Pytest by Kumar S

## Folder structure

- Section 3: Pytest 101: Create Project and First Test
  - `01-pytest-101/pytest_topics`
- Section 4: Pytest: Assertions and Test Discovery
  - `01-pytest-101/py_assertions`
- Section 5: Pytest: Skip/Mark and Pytest Options
  - `01-pytest-101/py_skip_mark`

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

[pytest xfail][https://docs.pytest.org/en/7.1.x/how-to/skipping.html#xfail-mark-test-functions-as-expected-to-fail]

similar to raising exception in the test, but `xfail` shows the better labels such as `XFAIL` or `XPASS`

```sh
# 01-pytest-101/py_skip_mark

ptw -vs .

# test_xfail.py::test_str04 XPASS (known issue)
# test_xfail.py::test_str05 XFAIL
```

</details>
