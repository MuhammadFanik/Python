# Default parameter values - If the function is called without an argument, it uses the default value
def greet(fname, lname, age=20):
    print(fname, lname, age)

greet("Harris", "Ali", 15)
greet("Ali", "Khan", 25)
greet("Alice", "Bob")


# DIFFERENT DATA TYPES
# Sending list as an argument
def my_func(fruits):
    for fruit in fruits:
        print(fruit)


my_fruits = ["apple", "banana", "cherry", "mango", "lemon"]
my_func(my_fruits)
print("\n\n")

# RETURNING DIFFERENT DATA TYPES - Functions can return any data type (lists, dictionaries, tuples, and more)
# A function that returns a list
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])



# Task - You are building a simple app that registers users. You want to separate concerns: getting input, validating it
# and saving it.
# 1- Write register_user() that calls: 1-get_input(), 2-validate_input(), 3-save_to_db()

def get_input(name):
    print("Name received:", name)
def validate():
    print("Name validated")
def save():
    print("Name is saved to database")

def reg_user():
    get_input("Harris")
    validate()
    save()

reg_user()