# 1. SYNTAX, VARIABLES, AND DATA TYPES.

"""
1.1. PYTHON SYNTAX
Python uses indentation (spaces or tabs) to define the structure of the code.
This makes the code more readable but requires strict adherence to indentation levels.
"""

def my_function():
    """
    A function to illustrate correct indentation in Python.

    This function prints "Hello, world!" to the console,
    and then throws an IndentationError because the second
    print statement is not indented correctly.

    TO CHECK ERROR : when uncomment else and print lines, it will throw an IndentationError
    """
    if True:
        print("Hello, world!")  # Correct indentation
    #else:
    #print("Incorrect indentation")  # This will throw an IndentationError


"""
1.2. VARIABLES
Variables are storage locations in memory, and Python allows you to dynamically type them (you don’t have to declare a type).
Variables can be changed or reassigned on the go, and Python is dynamically typed, 
meaning the type of a variable is interpreted at runtime.
"""
a = 10       # Integer
a = "hello"  # Now it's a string



"""
1.3. DATA TYPES: PYTHON HAS SEVERAL BUILT-IN TYPES

Primitive Data Types:

int: Whole numbers.
float: Decimal numbers.
str: Text (strings).
bool: True or False.

Compound Data Types:

list: Ordered, mutable collection of items.
tuple: Ordered, immutable collection of items.
set: Unordered, unique items.
dict: Key-value pairs.
"""

# Integers
age = 25

#Floats
height = 5.9

# String
name = "John"

# Boolean
is_active = True
is_active = False

# LIST
"""
Mutable: You can change, add, or remove elements.
Ordered: Maintains the order of elements.
Allows duplicates.
Can contain mixed data types.
Common methods: append(), remove(), sort(), extend().
"""
fruits = ["apple", "banana", "cherry"]
my_list = [1, 2, 3, 3, 4]
my_list.append(5)  # [1, 2, 3, 3, 4, 5]

#TUPLE
"""
Immutable: Once created, you cannot change its elements.
Ordered: Maintains the order of elements.
Allows duplicates.
Can contain mixed data types.
Typically used when you need an immutable sequence of data.
"""
coordinates = (10.0, 20.0)
my_tuple = (1, 2, 3, 3, 4)
my_tuple[0] = 5  # Error, as tuples are immutable


#SET
"""
Mutable: You can add or remove elements.
Unordered: Does not maintain any particular order.
Does not allow duplicates: Each element must be unique.
Fast membership testing, useful for operations like union, intersection, difference.
"""
unique_numbers = {1, 2, 3}
my_set = {1, 2, 3, 3, 4}  # Duplicate '3' is removed automatically
print(my_set) # {1, 2, 3, 4}


#DICTIONARY
"""
Mutable: You can add, change, or remove key-value pairs.
Unordered (till Python 3.6) but ordered in Python 3.7+ (keeps insertion order).
Keys must be unique, but values can be duplicated.
Fast lookups via keys, commonly used for mapping data.
"""
student = {"name": "Alice", "age": 21}
student['age'] = 26  # Updates the value for 'age'


"""
READ MORE : https://nuwan-abeywickrama.medium.com/python-basic-understanding-variables-and-data-types-b7fb5d2036bb
"""