# T Level Technical Qualification in Digital Production, Design and Development
# 2.1.1 Understand the use of, and need for, data types:
#   ● string
#   ● character
#   ● integer
#   ● real/float
#   ● Boolean


# Strings:
# Strings are used for textual data such as names, addresses, email addresses, etc.
# A string is called a string because it is a sequence of characters strung together.

name = 'John'  # Assign the string value 'John' to the variable called name.
print(name)

# A variable is called a variable because its value can change - i.e., it can vary.
name = 'Mary'
print(name)

# We can also use double quotation marks instead of single quotation marks in Python.
# This makes it convenient, e.g., for names that have an apostrophe.
# name = "d'Artagnan"
print("The newest musketeer is", name)


# Characters:
# In Python, there is no separate 'character' data type.
# Instead, a single character is treated as a string with a length of 1.

forename = 'John'
# M is just a single character, but it is treated just as a string.
initial = 'M'
surname = 'McKechnie'
print(forename, initial, surname)
# Here I've added a dot character to the initial so that it prints more nicely:
print(forename, initial + '.', surname)

# Note that when we join two strings together, this is called concatenation.
# In the above example we concatenate the string value of the variable initial with the
# literal string value '.'

# We can get the individual characters of a string using square brackets [].
print(forename[0])  # Prints 'J'
print(forename[1])  # Prints 'o'
print(forename[2])  # Prints 'h'
print(forename[3])  # Prints 'n'

# Notice that the numbers in the square brackets start at 0, not 1.
# String:   John
# Position: 0123


# Integers:
# An integer is a whole number that can be either positive, negative, or zero.
# For example: 1, 2, 0, and -1, but not 3.5.

age = 50  # Here we set the variable named age to the integer value of 50.
print(forename, 'is', age, 'years old.')

first_prize = 10000
# Notice that there's a space between the £ and 10000 when this is printed:
print('The first prize is £', first_prize)

# In the example below I have used formatted string in order to avoid the space.
# Note the f before the opening single quote and the variable name in curly braces:
#    {first_prize}.
print(f'The first prize is £{first_prize}')

# We can use underscores to make numbers like 93 million easier to read.
distance = 93_000_000
print('The distance from the Earth to the sun is', distance, 'miles.')


# Real or floating-point numbers:
# These refer to numbers that do have digits after the decimal point.
# They are called 'floating-point' because the decimal point can 'float',
# i.e., it can be placed anywhere relative to the significant digits of the number.

pi = 3.14
print('The approximate value of π is', pi)

# We can add, subtract, multiply and divide numbers using the following operators:
# Add: +
# Subtract: -
# Multiply: *
# Divide: /

print(1 + 1)
print(4 - 2)
print(6 * 2)
# Notice that this prints 3.0 (a floating-point number) and not 3 (an integer):
print(9 / 3)

# We can perform 'integer division' using // instead of /
print(9 // 3)  # This prints 3 (an integer) and not 3.0
print(15 // 6)  # This prints 2 because there are only two whole 6s in 15.

# We can also get the remainder when performing integer division using the % (modulus)
# operator. E.g., the following prints 3 because dividing 15 by 6 gives 2 with a
# remainder of 3.
print(15 % 6)  # We read this as "15 mod 6"

# Note that in some other programming languages, such as Java, % is called the remainder
# operator. This is similar to modulus but differs when the signs of the divisor (6) and
# dividend (15) differ.
print(15 % -6)  # Prints -3 in Python (but in Java 15 % -6 evaluates to 3).
print(-15 % 6)  # Prints 3 in Python (but in Java -15 % 6 evaluates to -3).
print(-15 % -6)  # Prints -3 Python (in Java -15 % -6 also evaluates to -3).

# Note: Due to the way computers represent floating-point numbers, they may not always
# be exactly accurate.
# For example, 0.1 + 0.2 might not exactly equal 0.3.
print(0.1 + 0.2)  # This prints 0.30000000000000004 and not simply 0.3

# Note: Python stores floating point numbers and integers differently in the computer's
# memory. So, even though the values are mathematically identical, the data type of 3 is
# integer, but 3.0 is a floating point number.


# Booleans:
# The name Boolean comes from the logician George Boole:
# https://en.wikipedia.org/wiki/George_Boole
# Boolean variables can have either the value True or the value False.
# Booleans are often used in conditions, such as if statements, to help the program make
# decisions based on certain criteria. We'll soon learn more about using if statements
# to make decisions in programs.

# In the examples below we use >= to test if the age is greater than or equal to the
# legal voting age for different countries in the UK. This comparison returns a Boolean
# value: True if the condition is met and False otherwise.

age = 17
print('For a person aged ', age)
# We expect age >= 16 to evaluate to True (17 is greater than 16):
print('Eligible to vote in Scotland:', age >= 16)
# We expect age >= 18 to evaluate to False (17 is less than 18):
print('Eligible to vote in England:', age >= 18)
print('Eligible to vote in Northern Ireland:', age >= 18)
print('Eligible to vote in Wales:', age >= 16)

# We can combine and modify boolean expressions using 'and', 'or' and 'not.
# Here is an example using 'and':
year = 1973
print('Year', year, 'within reign of Queen Elizabeth II:',
      year >= 1952 and year <= 2022)

# Python also lets us simplify expressions like year >= 1952 and year <= 2022
# as follows:
print('Year', year, 'within reign of Queen Elizabeth II:', 1952 <= year <= 2022)
