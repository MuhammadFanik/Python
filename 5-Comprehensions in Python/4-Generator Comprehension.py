# Syntax --> (expression for item in iterable if condition)

# Example 1: Generating even numbers using a generator
res = (num for num in range(1, 11) if num%2 == 0)
print(res)
print(list(res))