# Table of Contents

* [Intro](#intro)
* [Your first program](#your-first-program)
* [Syntax](#syntax)
* [Variables](#variables)
* [Loops](#loops)
* [Functions](#functions)
* [Data structures](#data-structures)
* [Formatting](#formatting)
* [Comprehensions](#comprehensions)

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
The most confusing difference for newcomers to the languae is significant whitespace.
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

Python supports most common formats for expressing numeric literals. `Ob`, `O0`, and `Ox` prefixes will create binary, octal, and hex literals respectively.
Float literals can be written in scientific notation using either `E` or `e`.
Any number literal can be written with underscores between digits that do not affect the value at all.
Underscores are used solely to make reading the number easier.

All of these variables are equal to each other:
```python
a = 0x2A
b = 0b10_1010
c = 4.2e1
d = 4_2
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
