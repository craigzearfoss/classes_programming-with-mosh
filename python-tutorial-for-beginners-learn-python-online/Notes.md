# Python Tutorials for Beginners - Learn Python Online
- Programming with Mosh
- [https://www.youtube.com/watch?v=yE9v9rt6ziw&t=28s](https://www.youtube.com/watch?v=yE9v9rt6ziw&t=28s)
- Oct 22, 2018

## Setup

Make sure PHP is installed and up-to-date.

[https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart)

```
sudo apt-get update && sudo apt-get upgrade
python3 -V
sudo apt install -y python3-pip
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```
**Python is case sensitive.**

Built in primitive types:
- Numbers  [integer / float / complex]  (Ex. 1000 or 4.99 or # 1 + 2j)
- Booleans  (Ex. True or False)
- Strings   (Ex. "Python Programming")

Use triple quotes for long strings, for example if there are multiple lines'. (Ex. """This is a long string ... blah blah blah.""")

Comments begin with a hash tag #.

Built in functions:
- len(<string>) - returns the number of characters in a string

Strings characters can be retrieved by square brackets:
```
course = "Python Programming"
course[0]       P                   - returns the first character
course[-1]      g                   - returns the last character
course[0:3]     Pyt                 - returns the first three characters
course[0:]      Python Programming  - if you don't specify the last index it will return the rest of the string
course[:3]      Pyt                 - if you don't specify the first index it begins at the start of the string
course[:]       Python Programming  - returns a copy of the string
```

Escape sequences - prefix a character with a backslash, for example \" for a double quote.
```
\", \' \\, \n (new line)
```

### Concatenating strings
```
greeting = "Hello there, " + first_name + " " + last_name
goodbye = f"So long, {first_name} {last_name}"
```
**You can put any expressions inside the curly braces.**

Everything in Python is an object and objects have methods that we can access using the dot notation.
```
print(course.upper())
```

### Useful string methods:
```
upper           strip           find            <string2> in <string>
lower           lstrip          replace         <string2> not in <string1>
title           rstrip
```

For integer division use a double slash //.

You can use augmented operations like +-, -=, *=, **=, etc.

Useful math functions:
```
round
abs
```

There is also a math module that can be imported.
```
import math
```
To find all of the function in the math module you can Google "python 3 math module".

input() is used to get input from the user.  You can specify a user prompt.
```
x = input("x: ")
```

Functions for converting variable types:
```
int(x)          float(x)        bool(x)         str(x)          
```

type(x) returns the type of a variable.

Boolean "falsy" values: "", 0, None

# Fundamentals of Programming

## Comparison Operators
Can be used with numbers of strings
```
==, >, <, >=, <=>, !=
```
The function ord() returns the numeric representation of a character.

## Conditional Statements
#### Example 1
```
temperature = 35
if temperatue > 30:
    print("It's warm")
    print("Drink water")
print("Done")
```
- Python uses indentation to determine which lines of code should be interpretted. So in the above code the print("Done") will always be printed regardless of whether or not the condition is true.
- The PEP 8 specification for indentation is four white spaces.
  
#### Example 2 - else if statements
```
temperature = 15
if temperatue > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    prihnt("It's nice")
else:
    print("It's cold")
print("Done")
```

## Ternary operator
```
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
```

## Logical Operators - and, or, not
#### Example 1
```
high_income = True
low_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
```
#### Example 2 - not Operator
```
high_income = True
low_credit = True
student = True
if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")
```
Boolean operators are short circuted. That means.
-  For **and** operators if one condition fails then the rest are not evaluated.
-  For **or** operators if one condition is true then the rest are not evaluated.

### Chaining Comparison Operators
#### In Python you can write the following condition
```
if age >= 18 and age < 65:
```
as the following
```
if 18 <= age < 65:
```

## For Loops
#### Example 1 - range without a starting index
```
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
```
The output is:
```
Attempt 1 .
Attempt 2 ..
Attempt 3 ...
```

#### Example 2 - range with a starting index
```
for number in range(1, 4):
    print("Attempt", number, (number) * ".")
```
The output is:
```
Attempt 1 .
Attempt 2 ..
Attempt 3 ...
```

#### Example 3 - range with a starting index and a step
```
for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")
```
The output is:
```
Attempt 1 .
Attempt 3 ...
Attempt 5 .....
Attempt 7 .......
Attempt 9 .........
```

#### Example 4 - break statement
```
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
```
Output:
```
Attempt
Successful
```

#### Example 5
```
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
```
Output:
```
Attempt
Attempt
Attempt
Attempted 3 times and failed
```

## Nested Loop
```
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
```

## Iterables
- An iterable type means that you can iterate over it or use it in a **for loop**.
- Iterable types include **range**, **string** and **list**.
- You can create your own iterable object.
#### Example 1 - string iteration
```
for x in "Python":
    print(x)
```
Output:
```
P
y
t
h
o
n
```

#### Example 2 - list iteration
```
for x in [1, 2, 3, 4]:
    print(x)
```
Output:
```
1
2
3
4
```

## While Loop
#### Example 1
```
number = 25
while number > 0:
    print(number) number //= 2   # divide the number in half
```
Output:
```
25
12
6
3
1
```
#### Example 2 - interactive while loop
```
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
```
#### Example 3 - wwhile loop with a break statement
```
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() != "quit":
        break
```
**Be careful not to create infinite loops, that is, loops that never end.

# Functions

#### Example 1 - no parameters
```
def greet:():
    print("Hi there")
    print("Welcome aboard")


greet()
```
After the function remove indent on the next line and add two line breaks.  This is what PEP 8 recommends.

#### Example 2 - with aparameters
```
def greet:(first_name, last_name):
    print(f"Hi there, {first_name} {last_name}")
    print("Welcome aboard")


greet("Mike", "Smith")
```
Note that **parameters** are the inputs that you define for your function and **arguments** are the actual values passed into the function.

Functions fall into two categories.
- Perform a task
- Return a value

All functions return a value by default so if you do not specify a return value then the value of **None** is returned.

#### Example 3 - function that returns a value
```
def get_greeting(name):
    return f"Hi, {name}"


message = get_greeting("Mike")
file = open("content.txt", "w")
file.write(message)
```

#### Example 4 - not assigning the return result to a variable
```
def increment(number, by):
    return number + by


print(increment(2, 1))
```

#### Example 4 - using keyword arguments
```
def increment(number, by):
    return number + by


print(increment(2, by=1))
```
Keyword arguments can be used to make your code more readable.

### Example 5 - default arguments
```
def increment(number, by=1):
    return number + by


print(increment(2))
```
**Optional parameters should always come after the required parameters.**

#### Example 6 - a variable number of arguments
- Prefix the argument with an *.
- This creates a variable that is a **tuple*.
- The only differences between a tuple and a list is the notation, that is parentheses () versus square brackets [] respectively **AND** that **tuples cannot be modified**.
- Tuples cannot be modified.
- Tuples are iterable.
```
def multiply(*numbers*):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
```
Note the indentation of the return line.

#### Example 7 **args to create a dictionary
- Used to pass arbitratry keyword arguments
- The variables passed are used to create an object called a **dictionary** that contains multiple key/value pairs.
- Note that you can access individual keys in a dictionary using square brackets.

```
def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="John", age=22)
```
#### A dictionary looks like below.
```
{'id': 1, 'name':, 'John', 'age': 22}
```

## Scope
- Refers to the region of code where a variable is defined.
- Below the **message** and **name** variables are defined in the **greet** function so if we try to access them outside of the scope of that function as shown it results in an error.
- The **message** and **name** variables are said to have a **local scope**.
- Local variables have a short lifetime and since they aren't used anywhere else they are eventually garbage collected.
- The variable **formal_name** below is a global variable and can be used anywhere in this file.
- Global variables stay in memory for a longer period of time are are not garbage collected as frequently so they should not be used often.  **Global variables are evil!**
- By default Python treats variables in a function as local even if there is a global variable with the same name.
```
formal_name = "John Doe"

def greet(name):
    message = "a"


print(message)
```
You can change a global variable inside of a function by using the **global <variable_name>** statement but this is a very bad practice.

# Debugging

# VSCode shortcuts - Windows
- [Home]             - beginning of line
- [End]              - end of line
- [Crtl][Home]       - beginning of file
- Ctrl][End]         - end of file
- [Alt][Arrow Up]    - select lines and then enter this to move the lines up
- [Alt][Arrow Down]  - select lines and then enter this to move the lines down
- [Ctrl][/]          - create a comment block by first selecting lines

# Fizz Buzz
Rules
- If the input is divisible by 3 it returns the string "Fizz"
- If the input is divisible by 5 it returns the string "Buzz"
- If the input is divisible by both 3 and 5 it returns the string "FizzBuzz"
```
def fizz_buzz(input):
    if input % 3 == 0:
        if input % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print("3: ", fizz_buzz(3))
print("5: ", fizz_buzz(5))
print("15:", fizz_buzz(15))
print("7: ", fizz_buzz(7))
```

Alternate Fiz Buzz implementation
```
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print("3: ", fizz_buzz(3))
print("5: ", fizz_buzz(5))
print("15:", fizz_buzz(15))
print("7: ", fizz_buzz(7))
```
