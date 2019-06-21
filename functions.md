# Functions

Functions in Python are defined using the `def` keyword.

```python
def foo(bar, baz):
    return bar + baz
```

This defines a function named `foo` that takes two arguments and returns their sum.

Default arguments can be added with an equals sign as such:

```python
def foo(bar, baz=42):
    return bar + baz
```

This function can be called with either one or two arguments.

Python also supports variable argument lists by prepending a `*` to the last non-keyword argument

```python
def foo(*bar):
    s = 0
    for v in bar:
        s += v

    return s
```

This function will take any number of arguments and return the sum of all of them. The arguments are collected in `bar` as a list.

When calling functions it is possible to provide arguments out of order or skip some.

```python
def greet(first_name, last_name='The Nameless', greeting='Hello'):
    print(greeting, first_name, last_name)
```

This function can be called with 1, 2, or 3 arguments, using defaults if not enough are supplied.
If you wanted to supply a first name and a greeting with no last name you can use keyword arguments.

```python
greet('Noah', greeting='Salutations') # prints "Salutations Noah The Nameless"
```

You can also collect a variable number of keyword arguments in a function with two `*`s.

```python
def var(**kwargs):
    print(kwargs)
```

Keyword arguments will be passed into the function as a [dictionary](data_structures.md#dictionaries).

```python
var(first='foo', second='bar') # prints "{'first': 'foo', 'second': 'bar'}"
```
