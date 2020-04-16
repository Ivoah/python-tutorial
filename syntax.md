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

Python also supports a number of other prefixes, such as `f` for [formatting](formatting.md#f-strings).

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
