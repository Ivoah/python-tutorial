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
