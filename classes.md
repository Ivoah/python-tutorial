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
