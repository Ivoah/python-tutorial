# Type hinting

While Python is a dynamically typed language and doesn't have explicit types, it does have type hinting.
When used with tools such as [mypy] it is possible to combine the flexibility of dynamic typing with the safety of static typing.

```python
def foo(bar: str) -> int:
    return len(bar)
```

This is a function that takes a string and returns an integer.
Type hints for function parameters are placed after a colon after the parameter name.
Type hints for function return values are placed after an arrow after the parameter list, but before the ending colon.

Python itself does nothing with the type hints.
It would be perfectly valid to pass a list to the `foo` function defined above.
Type hints are purely decorative unless used with an external tools such as [mypy].

It is also possible to access the type hints from within Python code.
The `__annotations__` attribute of the function contains all the type hinting information.

```python
def foo(bar: str) -> int:
    return len(bar)

print(foo.__annotations__) # prints "{'bar': <class 'str'>, 'return': <class 'int'>}"
```

[mypy]: http://mypy-lang.org/
