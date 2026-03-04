# A lambda function is a small anonymous function. A lambda function can take any number of arguments,
# but can only have one expression.

# Syntax --> lambda arguments: expression

# Ex1: Add 10 to argument num, and return the result --> Just one argument
res = lambda num : num + 10
print(res(25))

# Ex2: Multiply argument a with argument b and return the result --> Multiple arguments
res = lambda a, b : a*b
print(res(5, 8))