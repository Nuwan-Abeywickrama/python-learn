# FUNCTIONS OF PYTHON

"""
functions are a fundamental building block of code.
They allow you to group together a sequence of statements and execute them whenever you need,
thus promoting reusability, readability, and maintainability.

A function in Python is defined using the def keyword, followed by a function name, parentheses (), and a colon (:).
The code inside the function is indented to indicate that it belongs to the function.


Syntax:

def function_name(parameters):
    # Code block
    return value  # Optional

function_name: The name of the function, which follows standard naming conventions (e.g., lowercase letters and underscores).
parameters: Variables that act as inputs to the function (optional).
return value: The result the function sends back to the caller (optional). If return is not used, the function returns None by default.
"""
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


"""
FUNCTION, PARAMETERS AND ARGUMENTS

Parameters are the variables listed inside the parentheses in the function definition, and arguments are the actual values passed to the function when calling it.

Type of arguments:
1.  Positional Arguments
2.  Default Arguments
3.  Keyword Arguments
4.  *args and **kwargs (Variable-Length Arguments - *args | Variable-Keyword Arguments - **kwargs )

Restricting Arguments
5.   Restricting Arguments: Positional-Only or Keyword-Only Arguments
6.   Combining: Positional-Only and Keyword-Only Arguments

Return Statement
7.  Returning Multiple Values

Scope and Lifetime of Variables
8. Global and Local Variables

9.  Recursion
10. Lambda Functions
11. Nested Functions
12. Decorators
"""


# POSITIONAL ARGUMENTS
"""
The arguments are passed to the function based on their position.
The first argument is assigned to the first parameter, the second argument to the second parameter, and so on.
"""
def add(a, b):
    print ("a = ", a,"\nb = ", b)
    return a - b

print(add(3, 4))  # 3 and 4 are positional arguments.

print(add(4, 3))  # Change the position of the values to see the output.


# DEFAULT ARGUMENTS
"""
You can assign default values to parameters. If the caller does not pass an argument, the default value is used.
"""
def greet_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_default("Alice"))  # Output: Hello, Alice!

print(greet_default("Bob", "Welcome")) # Change default value to 'Welcome'.  Output: Hi, Bob!


# KEYWORD ARGUMENTS
"""
The arguments are passed to the function based on their names. Arguments passed with the 'name=value' syntax are assigned to the corresponding parameter.
Keyword Arguments are used when the order of the arguments is not important.
"""
def greet_keyword(name, greeting):
    return f"{greeting}, {name}!"

print(greet_keyword(name="Alice", greeting="Hi"))  # Output: Hi, Alice!

print(greet_keyword( greeting="Welcome", name="Alex"))  # Output: Welcome, Alex!


# VARIABLE-LENGTH ARGUMENTS (*args)
"""
Variable-Length Arguments allow a function to accept an arbitrary number of positional arguments. 
This is done using *args in the function definition, where args is just a convention (you can name it anything, but the * symbol is required).
"""
def sample(*args):
    return sum(args)

def add(*numbers):
    print("VARIABLE LENGTH ARGUMENTS", numbers)
    return sum(numbers)

print(add(1,2,3,4,5))  # Output: 15


# VARIABLE-KEYWORD ARGUMENTS (**kwargs)
"""
Variable-Keyword Arguments allow a function to accept an arbitrary number of keyword arguments. 
This is done using **kwargs in the function definition, where kwargs is just a convention (you can name it anything, but the ** symbol is required).
"""
def sample(**kwargs):
    return kwargs

def greet_with_keyword_arguments(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, anonymous!")


greet_with_keyword_arguments(name="Alien", age=25)  # Passing keyword arguments - Output: Hello, Alien!

greet_with_keyword_arguments()  # No keyword arguments - Output: Hello, anonymous!


# RESTRICTING ARGUMENTS: POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
"""
Python provides two ways to restrict how arguments can be passed: Positional-only arguments and Keyword-only arguments. 
You can use special syntax to enforce these restrictions.
"""

# POSITIONAL-ONLY ARGUMENTS
"""
To define positional-only arguments, you use the / symbol in the function signature. 
Any argument before / can only be passed positionally and not as a keyword argument.
"""
def greet_with_positional_only_arguments(name, /, greeting):
    return f"{greeting}, {name}!"

print(greet_with_positional_only_arguments("Alice", "Hello"))  # Output: Hello, Alice!

print(greet_with_positional_only_arguments("Bob", greeting="Hi"))  # Output: Hi, Bob!

print(greet_with_positional_only_arguments(name="Alice", greeting="Hi"))  # TypeError | Error: 'name' must be passed positionally, cannot use as a keyword argument.


# KEYWORD-ONLY ARGUMENTS
"""
To define keyword-only arguments, you use the * symbol in the function signature. 
Any argument after * can only be passed as a keyword argument and not positionally.
"""
def greet_with_keyword_only_arguments(*, name, greeting):
    return f"{greeting}, {name}!"

print(greet_with_keyword_only_arguments(name="Alice", greeting="Hi"))  # Correct: 'name' must be passed as a keyword argument | Output: Hi, Alice!

print(greet_with_keyword_only_arguments("Alice", "Hi"))  # TypeError | Error: 'name' must be passed as a keyword argument, not positionally.

print(greet_with_keyword_only_arguments("Alice", greeting="Welcome")) # TypeError | Error: Both 'name' and 'greeting' must be passed as a keyword arguments.


# COMBINING POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
"""
You can combine both positional-only and keyword-only arguments in a single function signature.

The / makes a positional-only argument.
The * makes a keyword-only argument.
"""
def process_data(data, /, *, verbose=False):
    if verbose:
        print("Verbose mode on")
    print(f"Processing {data}")

process_data([1, 2, 3], verbose=True)  # Correct | 'data' is positional-only, 'verbose' is keyword-only

process_data(data=[1, 2, 3], verbose=True)  # TypeError | Error: 'data' cannot be passed as a keyword argument

process_data([1, 2, 3], True)  # TypeError | Error: 'verbose' must be passed as a keyword argument



# RETURNING MULTIPLE VALUES
"""
In Python, you can return multiple values by separating them with commas. 
Python implicitly packs these values into a tuple, which can then be unpacked by the caller.
"""
def get_person_info():
    name = "Alice"
    age = 30
    city = "New York"
    return name, age, city  # Returns a tuple

person_name, person_age, person_city = get_person_info() # Unpacking the returned tuple into separate variables

print(person_name)  # Output: Alice
print(person_age)   # Output: 30
print(person_city)  # Output: New York


# GLOBAL AND LOCAL VARIABLES
"""
In Python, global and local variables are distinguished based on their scope, 
which determines where the variables can be accessed and modified in a program.
"""

# LOCAL VARIABLES
"""
A local variable is a variable that is defined inside a function and can only be accessed within that function.
It is created when the function is called and destroyed when the function exits.
Local variables cannot be accessed outside the function they are defined in.
"""
def local_example():
    x = 10  # Local variable
    print(f"Inside function: {x}")

local_example()  # Output: Inside function: 10
# print(x)  # Error: 'x' is not defined outside the function


# GLOBAL VARIABLES
"""
Global variables are variables that are defined outside of a function and can be accessed and modified from anywhere in the program.

A global variable is defined outside of all functions, typically at the top of a script, and can be accessed by any function or block of code in the program.
Global variables exist for the entire lifetime of the program and can be accessed anywhere after they are declared.
You can read global variables inside a function, but to modify a global variable inside a function, you must declare it as global.

NOTE : To modify a global variable inside a function, you must declare it using the global keyword. 
Otherwise, Python will assume you are creating a new local variable within the function.
"""
y = 20  # Global variable
def global_example():
    print(f"Accessing global variable inside function: {y}")

global_example()  # Output: Accessing global variable inside function: 20
print(f"Outside function: {y}")  # Output: Outside function: 20

# MODIFYING GLOBAL VARIABLES INSIDE FUNCTIONS

z = 5  # Global variable
def modify_global():
    global z  # Declare z as global to modify it
    z = 10
    print(f"Inside function, modified z: {z}")

modify_global()  # Output: Inside function, modified z: 10
print(f"Outside function, modified z: {z}")  # Output: Outside function, modified z: 10
