# Loops

Python supports `for` and `while` loops.

## For loops

`For` loops operate a little differently than what you might be used to in C or Java.
They are similar to Java's "enhanced" `for` loops in that they traverse over an iterator.

```python
for i in range(10):
    print(i)
```

This code will print every number between `0` (inclusive) and `10` (exclusive).
The `range` function returns an iterator that goes from `0` to `9` and the `for` loop will run once for every value in the iterator.

`range` can accept a start, end, and step value. `range(5, 13, 2)` will loop over `[5, 7, 9, 11]`.

A `for` loop can traverse any iterable, such as a [list](data_structures.md#lists) or generator.

```python
l = [8, 9, 2, 'hi']
for item in l:
    print(item)
```

This code will print every item in the list on its own line

## While loops

`While` loops are far more conventional in Python.
They simply take a boolean expression and continue to execute while it's true.

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

## Else clause

Both `for` and `while` loops support an optional `else` clause.
The code in the `else` clause is only executed if the loop ended normally, i.e. `break` was not called.

```python
for name in names:
    if name == 'Jebediah':
        print('Found Jeb!')
        break
else:
    print("Jeb wasn't in the list of names")
```
