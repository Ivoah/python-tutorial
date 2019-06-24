# Exceptions

Exceptions in Python are handled using `try`/`except` blocks.

```python
try:
    # Code that could throw an exception
except:
    # Handle exception
```

This code will catch any error that is thrown inside the `try` block. It is possible to narrow down the exceptions that the `except` block will catch.

```python
try:
    # Code that could throw an exception
except IndexError:
    # Handle only an IndexError
```

If you need the exception object it is also possible to give it a name so it can be referenced in the `except` block.

```python
try:
    # Code that could throw an exception
except IndexError as e:
    # Handle only an IndexError
```

`Try`/`except` statements also support `else` and `finally` clauses. An `else` clause after `try`/`except` will execute only if the `except` clause does not run. A `finally` clause will always run, regardless if an exception is thrown or not.

```python
try:
    # Code that could throw an exception
except:
    # Handle exception
else:
    # Only runs if except clause doesn't
finally:
    # Always runs
```

`Finally` clauses are usually used to clean up resources used in a `try` block.
