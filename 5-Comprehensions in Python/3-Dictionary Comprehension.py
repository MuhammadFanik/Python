# Syntax --> {key_expression: value_expression for item in iterable if condition}
# key_expression --> Determines the dictionary key
# value_expression --> Computes the value
# Iterable --> The source collection
# conditional --> Filters elements before adding them

# Example 1: Creating a dictionary of numbers and their cubes
nums = {num:num**3 for num in range(1, 8)}
print(nums)


# Example 2: Mapping states to capitals
a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital
result = {state: capital for state, capital in zip(a, b)}
print(result)