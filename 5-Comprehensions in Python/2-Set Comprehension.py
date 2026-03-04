# Syntax --> {expression for item in iterable if condition}

# 1- Create a set of numbers from 0 to 9.
num = {number for number in range(10)}
print(num)

# 2- Generate a set of squares of numbers from 1 to 10.
squares = {number**2 for number in range(1, 11)}
print(squares)

fav_chais = ["Masala Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai"]
unique_chais = {chai for chai in fav_chais}
print(unique_chais)


recipes = {
    "Masala Chai": ["Cardamom", "Clove", "Ginger"],
    "Pink Tea": ["Milk", "Pink tea powder", "Sugar"],
    "Cardamom Tea": ["Cardamom", "Milk", "Sugar"]
}

uniques = {spice for ingredients in recipes.values() for spice in ingredients}
print(uniques)