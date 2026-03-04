# Syntax --> [expression for item in iterable if condition]

# List of squares of numbers from 0 to 4
squares = [x**2 for x in range(5)]
print(squares)

# Squares of even numbers from 0 to 10
even = [x**2 for x in range(11) if x%2 == 0]
print(even)

# Convert the list ['apple', 'banana', 'cherry'] to a list of uppercase strings using list comprehension.
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)