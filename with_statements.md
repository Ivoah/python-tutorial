# With statements

`With` statements enable files (and other objects) to automatically be closed when they are no longer needed.

```python
with open('file.txt') as f:
    print(f.read())
```

The file `f` will automatically be closed at the end of the `with` statement's code block
