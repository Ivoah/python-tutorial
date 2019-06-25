# String formatting

Python supports 3 different ways to format strings.
The first method is similar to C-style printf formatting, while the second two are different.

## % formatting

Python supports C-style printf formatting using the `%` operator.

```python
print('%s - %d' % ('foo', 42)) # prints "foo - 42"
```

Use of this style of formatting is discourage in favor of the two newer methods.

## .format

In addition to C-style formatting, Python also has a new style for formatting strings.

```python
print('{} - {}'.format('foo', 42)) # prints "foo - 42"
```

Each `{}` in the source string is a placeholder that is filled by an argument passed to `.format()`.
The placeholders can also be named and filled in using keyword arguments passed to `.format()`.

```python
print('{name} is {age} years old'.format(age=21, name='Noah')) # prints "Noah is 21 years old"
```

## f-strings

Python's third main string formatting tool is f-strings.
By prepending a `f` to a string literal you can make it an f-string, which allows variable names to be inserted directly into the string.

```python
name = 'Noah'
age = 21
print(f'{name} is {age} years old') # prints "Noah is 21 years old"
```

## Advanced formatting

Both `.format()` and f-strings support advanced formatting of their arguments.
The general syntax is as such:

```
{[name or variable]:[options]}
```

The most useful is controlling how many digits are printed after a decimal point.

```python
long_number = 42.5838294585
print(f'{long_number:.3f}') # prints "42.584"
```

## Further reading

Much more information about formatting can be found at https://pyformat.info/
