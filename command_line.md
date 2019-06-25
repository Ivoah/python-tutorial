# Command line arguments

Python has multiple ways to use command line arguments passed to the script.

## sys.argv

The simplest (and best for scripts that don't really take options) is to just read the raw strings passed to the python process.

```python
import sys

print(sys.argv[0]) # prints name of script
print(sys.argv[1]) # prints 1st argument
...
```

All arguments passed to Python are collected in `sys.argv`.
The first item is the path of the script that was passed to python.
All subsequent items are the remaining arguments passed.
Since `sys.argv` is just a list it is important to check the size before accessing elements, or surround accesses in `try`/`except` blocks in case the wrong number of arguments were passed.

## argparse

The more complicated, but much more flexible, way of handling command line arguments is to use Python's built in module `argparse`.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
args = parser.parse_args()

print(f'foo = {args.foo}')
```

When run with `python args.py --foo bar` this program will print out `"foo = bar"`

This is only a very simple example of `argparse`.
It is much more powerful, and a full tutorial can be found in the [official documentations](https://docs.python.org/3/howto/argparse.html)
