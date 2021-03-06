# Table of Contents

* [Intro](#intro)
* [Your first program](#your-first-program)
* [Syntax](#syntax)
* [Variables](#variables)
* [Loops](#loops)
* [Functions](#functions)
* [Data structures](#data-structures)
* [Classes](#classes)
* [Exceptions](#exceptions)
* [String formatting](#string-formatting)
* [File I/O](#file-io)
* [With statements](#with-statements)
* [Command line arguments](#command-line-arguments)
* [Comprehensions](#comprehensions)
* [Type hinting](#type-hinting)
* [C Interop](#c-interop)

# Intro

This guide is written for an audience who is already familiar
with languages such as C and Java.

## Installing

Install the latest version of Python 3 from [python.org](https://www.python.org/downloads/).
Be sure to install Python 3 and not Python 2.
Python 2 is deprecated and will not be maintained past January 1 2020.
No new code should be written in Python 2.

When installing be sure to add Python to the PATH so you can run scripts
from the command line.

Open up a command prompt and run `python` to ensure that Python is installed correctly.
You should be greeted with a welcome message which includes the version of Python running.
Ensure that this version number matches the one you installed.
Type `exit()` to leave the interactive prompt.

You can open an interactive prompt at any time to test out small snippets of code without having to make a new script.

# Your first program

The simplest Python program is just an empty text file.
Python doesn't require any special functions or objects to be created unlike C or Java.
The Python iterpreter will simply execute each line in the source file starting at the top.

As is tradition, your first Python program will simply print `Hello world`.

```python
print('Hello world')
```

Save this file as `hello.py` and run it on the command line with `python hello.py`.
If you installed Python correctly then you should see `Hello world` printed and be returned to your prompt.

# Syntax

Python syntax shares many similarities with languages such as C and Java.

## Indentation
The most confusing difference for newcomers to the language is significant whitespace.
Unlike most languages, Python uses indentation to separate blocks instead of curly braces or other identifiers.

```python
def foo():
    print('bar')
print('baz')
```

In this example `foo()` is a function that will print out `bar` when it is run.
The line that prints `"baz"` is not a part of the function, because it is not indented to the same level.
Many editors will display guides in the gutter to assist with keeping track of what block a particular line belongs to.

Indentations should always be made using spaces; indenting with tabs is highly discouraged unless it is done to remain consistent with existing code.

## Literals

### Strings

String literals are written Python with either single or double quote characters. `foo = 'bar'` and `foo = "bar"` are identical in function.
Convention is to use single quotes unless a single quote appears in the string itself.
When a quote character appears in a string it is easiest to use the other type of quote when making the string. It is also possible to just escape the contained quote.
Both `foo = 'bar\'baz'` and `foo = "bar'baz"` create the same string.

Python also supports raw strings which cannot have escape sequences in them. This is useful when a string would have many backslashes in it, such as a regex pattern.
```python
patt = r'\d+(\.\d\d)?'
```
Notice the `r` prepended to the string which indicates a raw string.
Without using a raw string this same pattern would have to look like this:
```python
patt = '\\d+(\\.\\d\\d)?'
```
This obscures the original meaning of the string when being read.

Python also supports a number of other prefixes, such as `f` for [formatting](#f-strings).

### Numbers

Python supports most common formats for expressing numeric literals. `0b`, `0o`, and `0x` prefixes will create binary, octal, and hex literals respectively.
Float literals can be written in scientific notation using either `E` or `e`.
Any number literal can be written with underscores between digits that do not affect the value at all.
Underscores are used solely to make reading the number easier.

All of these variables are equal to each other:
```python
a = 0x2A
b = 0o52
c = 0b10_1010
d = 4.2e1
e = 4_2
```

# Variables

In Python variables can hold any type of value; it does not even have to be the same across a variable's lifetime.
Variables in Python do not need to be defined prior to being assigned to.

```python
foo = 'bar'
```

This snippet makes a new string variable with the value `'bar'`.

Just about anything in Python can be assigned to a variable and passed around as such.

```python
foo = print
foo('Hello world')
```

This program will print `Hello world` just as if the print function had been called directly.

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

A `for` loop can traverse any iterable, such as a [list](#lists) or generator.

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

Keyword arguments will be passed into the function as a [dictionary](#dictionaries).

```python
var(first='foo', second='bar') # prints "{'first': 'foo', 'second': 'bar'}"
```

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
original[::2] = [7]*int(len(original)/2) # replace every other value with 7
```

## Tuples

A tuple in Python is basically an immutable list. Tuples are created using parentheses.

```python
t = (3, 4)
```

Like lists they can store any values and be heterogeneous.
They also support all the same features as lists aside from changing elements.

Tuples are typically used when returning multiple values from a function.

```python
def foo(a, b):
    return a/b, a%b
```

The function `foo` in the block above returns a tuple with two values in it.
Notice the parentheses are not necessary in this context.

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

# Classes

Python is an object oriented programming language.
Accordingly, it is possible to create custom classes and define methods on them.
New classes are defined using the `class` keyword.

```python
class Adder:
    def __init__(self, initial_total):
        self.total = initial_total
    
    def add(self, n):
        self.total += n

foo = Adder(5)
print(foo.total) # prints "5"
foo.add(10)
print(foo.total) # prints "15"
```

This code creates a simple class with two methods defined.
`__init__` is a special ["dunder" method](#dunder-methods) which acts as the class's initializer.
This initializer takes two arguments: `self`, which is a reference to the new instance of the class, and `initial_total`, used to initialize `self.total`.
All methods must have at least one parameter, conventionally called `self`, so they can reference the class they are part of.

Python has no concept of public vs. private members of a class.
Conventionally "private" members of a class are prefixed with an underscore, but this is purely convention and they are still accessible from outside the class.

## Dunder methods

Python doesn't support overloading operators to provide advanced functionality to classes, but instead uses special double underscore, or dunder, methods.

Some of the most common are `__init__`, `__str__`, `__lt__`, `__gt__`, and `__getitem__`.

A full list of dunder methods and their usage can be found in the [official documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names)

# Exceptions

Exceptions in Python are handled using `try`/`except` blocks.

```python
try:
    # Code that could throw an exception
except:
    # Handle exception
```

This code will catch any error that is thrown inside the `try` block.
It is possible to narrow down the exceptions that the `except` block will catch.

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

`Try`/`except` statements also support `else` and `finally` clauses.
An `else` clause after `try`/`except` will execute only if the `except` clause does not run.
A `finally` clause will always run, regardless of whether an exception is thrown or not.

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
Alternatively use [with statements](#with-statements) to handle it automatically.

# With statements

`With` statements enable files (and other objects) to automatically be closed when they are no longer needed.

```python
with open('file.txt') as f:
    print(f.read())
```

The file `f` will automatically be closed at the end of the `with` statement's code block

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

# C Interop

Python has numerous ways to interoperate with C code.
`ctypes` is a built in module, but becomes messy for anything other than trivial usage.
`cffi` is a third party module that makes C interop much simpler and streamlined.
The third option is to write a python module directly in C. This method doesn't offer much benefit over using `cffi` and is far more involved to set up.

## CFFI

`cffi` has two modes of operation.
`ABI` mode and `API` mode.
`ABI` mode is very easy to use, but can more easily fail at runtime if types are not defined correctly.
`API` mode works by creating a python module in C and compiling it along with whatever library or sources you are trying to access through python.
The disadvantage to this method is the requirement for a C compiler and an extra step to compile the module.
It is marginally faster when making calls to C code however.
It should be used when you anticipate making many time sensitive calls to C code.
Otherwise `ABI` mode is probably sufficient.

The following data were taken by running a fibonacci function implemented in both C and Python 1,000,000 times.
Across multiple runs `ctypes` and `cffi (ABI)` times were nearly identical, with `cffi (API)` being faster, and the pure Python implementation being the slowest.
When calculating a large fibonacci number once, all three C implementations were comparable.

```
ctypes:        0.5116191999995863
cffi (ABI):    0.49985519999972894
cffi (API):    0.2513962000002721
python:        10.211897299999691
```

### ABI mode

The following code loads a shared library called `lib.so` and calls a function `foo` inside it.
The most important part of this code is the call to `ffi.cdef()`. This tells `cffi` what functions are defined in the library and what their signatures are.
The string passed is straight C code that can be pulled out of a header file.
Being straight C code, the ending semicolon is important.

```python
from cffi import FFI

ffi = FFI()
lib = ffi.dlopen('./lib.so')
ffi.cdef('int foo(int bar);')

print(lib.foo(7)) # call foo() from the C library
```

### API mode

Using the API mode of `cffi` is more involved.
First you must create a separate script that will create and compile the Python module.
The following script is an example for a hypothetical library in `foo.c`.
Running `foo_extension_build.py` will create `_foo.c`, `_foo.o` and `_foo.so`.
The last file is the actual library that can be imported by Python.
The second snippet shows how to import and use this shared library.

`foo_extension_build.py`:
```python
from cffi import FFI

ffi = FFI()
ffi.cdef('int foo(int bar);')
ffi.set_source('_foo', '#include "foo.h"', sources=['foo.c'], libraries=[])

if __name__ == '__main__':
    ffi.compile(verbose=True)
```

```python
from _foo.lib import foo

print(foo(7)) # call foo() from the C library
```
