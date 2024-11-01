# CONTROL STRUCTURES (CONDITIONALS AND LOOPS)

"""
CONDITIONALS

if, elif, and else statements allow the program to make decisions.

Syntax:

if condition:
    # code block if the condition is True
elif another_condition:
    # code block if the another condition is True
else:
    # code block if all above conditions are False

if statement: Executes if the condition is True.
elif (else if): Additional conditions checked if the previous "if" or "elif" was False.
else statement: Executes when none of the previous conditions are met.
"""
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


# Chaining Comparisons
age = 18
if 18 <= age < 65:
    print("Working age")

# Compound Conditions
temperature = 25
good_oxygen_level = True

if temperature > 20 and good_oxygen_level:
    print("Comfortable Environment")


"""
LOOPS

For Loop: The for loop iterates over items of a sequence (like a list, tuple, or string) and executes a block of code for each item.
While Loop: The while loop keeps executing a block of code as long as a specified condition remains true.
"""

# FOR LOOP
my_list = [1, 2, 3, 4, 5]
for num in my_list: # Iterate through a list
    print(num)

# Looping with enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)  # Outputs index and fruit

# Looping with range
for i in range(3):# Iterate through a range of numbers
    print(i)  # Outputs 0, 1, 2

for i in range(0, 10, 2):
    print(i)    # Outputs 0, 2, 4, 6, 8


# WHILE LOOP
count = 0
while count < 3:
    print(count)
    count += 1

# WHILE Loop with ELSE
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed without break")

#  OUTPUT:
#  0
#  1
#  2
#  3
#  4
#  Loop completed without break



# BREAK, CONTINUE, PASS
"""
break: Exits the loop completely.
continue: Skips the rest of the code in the current iteration and moves on to the next iteration.
pass: The pass statement is a null operation; nothing happens when it is executed.
"""

for i in range(10):
    if i == 5:
        break
    print(i)  # Outputs: 0, 1, 2, 4


for i in range(10):
    if i == 5:
        continue
    print(i)  # Outputs: 0, 1, 2, 3, 4, 6, 7, 8, 9


for i in range(5):
    if i == 5:
        pass  # No action taken when "i" is 5, just a placeholder
    print(i)

    #  OUTPUT: 0, 1, 2, 4, 5, 6, 7, 8, 9



"""
READ MORE : https://nuwan-abeywickrama.medium.com/control-structures-in-python-conditional-statements-and-loops-41f0042583fa
"""