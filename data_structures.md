# Data Structures

Python has some very powerful data structures

## Lists

Python's simplest data structure is a list.
New lists can be created with square brackets.
Items in a list are not constrained to be of the same type; a list can hold absolutely anything.

```python
l = [5, 2, 3, ['foo', 'bar', 42, 5, 5], 3]
```

In this example `l` is a list with 5 elements. 

The length of a list is accessed with the `len` function.

```python
print(len([4, 5, 6])) # prints "3"
```

Items from a list are accessed with the conventional bracket syntax.

```python
def second(l):
    return l[1]
```

This function will return the second item in the list (and throw an error if it's shorter than that).

### Slices

Python also has a slice syntax that allows more advanced selections from lists.

```python
list[start:stop:step]
```

The `start`, `stop`, and `step` arguments are the same as in the `range` function.
Any omitted parts use default values: 0 for the start, length for the stop, and `1` for the step.
The new list that is returned is a shallow copy of the original.

Slicing allows for some neat tricks:

```python
copy = original[:] # Creates a shallow copy of original list
reverse = original[::-1] # Creates a copy that is reversed
```

It is even possible to change chunks of a list by assigning with slices

```python
original[::2] = [7]*len(original) # replace every other value with 7
```

## Tuples

A tuple in Python is basically an immutable list. Tuples are created using parentheses.

```python
t = (3, 4)
```

Like lists they can store any values and be heterogeneous.
They also support all the same features as lists aside from changing elements.

## Dictionaries

One of Python's most powerful data structure is the dictionary.
Python's dictionary is equivalent to Java's HashMap.
Dictionaries are created using curly braces.

```python
d = {'key 1': 'value 1', 'key 2': 'value 2'}
```

Accessing items from dictionaries looks just like list access.

```python
d = {'key 1': 'value 1', 'key 2': 'value 2'}
print(d['key 2']) # prints "value 2"
```

Iterating over a dictionary will iterate over its keys

```python
d = {'key 1': 'value 1', 'key 2': 'value 2'}
for key in d:
    print(key, d[key]) # prints every key and value in d
```

It is possible to iterate over both keys and values at the same time using the `.items()` method.

```python
d = {'key 1': 'value 1', 'key 2': 'value 2'}
for key, value in d.items():
    print(key, value) # prints every key and value in d
```

Again as with lists and tuples dicts can be heterogenous.

```python
def foo():
    print('foo')

def bar():
    print('bar')

d = {'f1': foo, 'f2': bar, 'number': 23}

d['f1']() # calls the function "foo" defined above
```
