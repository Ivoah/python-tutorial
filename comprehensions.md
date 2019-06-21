# Comprehensions

Some of Python's coolest features are list, dictionary, and generator comprehensions.
These allow you to create complex lists and dictionaries using a concise syntax.

## List Comprehensions

List comprehensions are created as such:

```python
new_list = [<expression> for <variable> in <iterable>]
```

The following two lists are identical

```python
list1 = []
for i in range(10):
    list1.append(i*2)

list2 = [i*2 for i in range(10)]
```

List comprehensions also allow you to filter the data before it is passed to the expression.

```python
new_list = [i*2 for i in range(10) if i%2 == 0]
```

This lets the list comprehension replace both `map` and `filter` in a functional programming style.

## Dictionary Comprehensions

Dictionary comprehensions are nearly identical to list comprehensions, except they create a dictionary instead of a list.

```python
new_dict = {f'key #{i}': i for i in range(10)}
```

Dictionary comprehensions also support filtering

## Generator Expressions

Generator expressions are exactly the same as list comprehensions except they return a generator and are created with parentheses instead of brackets.

```python
new_gen = (i*2 for i in range(10))
```

One shortcut with generator expressions is you can omit the parentheses if the generator is the only argument to a function.

```python
print('\n'.join(str(i*2) for i in range(10)))
```
