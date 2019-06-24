# File I/O

File I/O is incredibly easy in Python.
A file object is created by calling the `open()` function.
At its simplest `open()` takes a single argument, the name of the file to open.

File objects have numerous methods for reading the contents of the file. Additionally, a file object can be iterated over directly, yielding complete lines.

```python
f = open('file.txt')
content = f.read()
f.close()
```

```python
f = open('file.txt')
lines = f.readlines()
f.close()
```

```python
f = open('file.txt')
for line in f:
    ...
f.close()
```

A complete list of file methods can be found in the [official documentation](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects)

When opening a file for writing just pass `'w'` as the second argument to `open()`.

```python
f = open('file.txt', 'w')
f.write('Test message')
f.close()
```

Be sure to close file objects when you are done using them to prevent resource leaks.
Alternatively use [with statements](with_statements.md#with-statements) to handle it automatically.
