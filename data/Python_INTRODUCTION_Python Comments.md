
# Python Comments

A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

## Single-Line Comments:

To write a comment just add a ‘#’ at the start of the line.

**Example 1:**

```python
#This is a 'Single-Line Comment'
print("This is a print statement.")
```



Output:

```markup
This is a print statement. 
```



**Example 2:**

```python
print("Hello World !!!") #Printing Hello World
```


Output:

```markup
Hello World !!!
```


**Example 3:**

```python
print("Python Program")
#print("Python Program")
```


Output:

```markup
Python Program
```


## Multi-Line Comments:

To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

**Example 1:** The use of ‘#’.

```python
#It will execute a block of code if a specified condition is true.
#If the codition is false than it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```


Output:

```markup
p is greater than 5.
```



**Example 2:** The use of multiline string.

```python
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```


Output:

```markup
p is greater than 5.
```
# Multiple Choice Questions on Python Comments

### Question 1:
Which of the following symbol is used to write a single-line comment in Python?  
- A. `//`  
- B. `#`  
- C. `/*`  
- D. `<!--`  

---

### Question 2:
What is the output of the following code snippet?  
```python
print("Python") 
# print("Commented Out")
```
- A. Python
- B. Python Commented Out
- C. Commented Out
- D. Error

