
# C++ Data Types & Constants

### C++ Data Types

Data types define the type of data a variable can hold; for example, an integer variable can hold integer data, a character can hold character data, etc.

Data types in C++ are categorized into three groups:

#### Built-in data types

These data types are pre-defined for a language and could be used directly by the programmer.

Examples are: Int, Float, Char, Double, Boolean

#### User-defined data types

These data types are defined by the user itself.

Examples are: Class, Struct, Union, Enum

#### Derived data types

These data types are derived from the primitive built-in data types.

Examples are: Array, Pointer, Function

Some of the popular built-in data types and their applications are:

| Data Type | Size         | Description                                                                 |
|-----------|--------------|-----------------------------------------------------------------------------|
| int       | 2 or 4 bytes | Stores whole numbers, without decimals                                      |
| float     | 4 bytes      | Stores fractional numbers, containing one or more decimals. They require 4 bytes of memory space. |
| double    | 8 bytes      | Stores fractional numbers, containing one or more decimals. They require 8 bytes of memory space. |
| char      | 1 byte       | Stores a single character/letter/number, or ASCII values                   |
| boolean   | 1 byte       | Stores true or false values                                                |


### C++ Constants

Constants are unchangeable; when a constant variable is initialized in a program, its value cannot be changed afterwards.

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    const float PI = 3.14;
    cout << "The value of PI is " << PI << endl;
    PI = 3.00; //error, since changing a const variable is not allowed.
}

```


Output:

```cpp
error: assignment of read-only variable 'PI'
```