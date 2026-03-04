# TUPLES ARE IMMUTABLE
# TUPLES ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE
# TUPLE ITEMS ARE ORDERED, UNCHANGEABLE, AND ALLOW DUPLICATES
# ORDERED --> ITEMS HAVE A DEFINITE ORDER AND IT WONT CHANGE
# UNCHANGEABLE --> ITEMS CANNOT BE CHANGED, ADDED, OR REMOVED AFTER A TUPLE IS CREATED
# TUPLE ITEMS CAN BE OF ANY DATA TYPE AND A TUPLE CAN CONTAIN MULTIPLE DATA TYPES ELEMENTS

this_tuple = ("Arijit", "Atif", "KK", "Sonu", "Shreya")
print(f"This Tuple: {this_tuple}")

# Tuple length
print(f"Length of this_tuple: {len(this_tuple)}")

# Access Tuple Items
print(f"First item in this_tuple: {this_tuple[0]}")

# Check if item exists
print(f"Is Atif in this_tuple? {"Atif" in this_tuple}")


# UPDATE TUPLES - You cannot change, or add, or remove items once a tuple is created. But there are some workarounds
# You can convert a tuple into a list and then make the changes and then covert it back into a tuple
this_tuple_list = list(this_tuple)
this_tuple_list.append("Armaan Malik")
this_tuple = tuple(this_tuple_list)
print(this_tuple)


# UNPACK TUPLES - The number of variables must match the number of values in the tuple. If not, then use an * to collect the
# remaining values
green, yellow, red = ("Apple", "Banana", "Strawberry")
print(green)


# LOOP TUPLES
num_tuple = (2, 5, 7, 8, -8, 11)
for i in num_tuple:
    print((i))


# JOIN TUPLES
even = (2, 4, 6, 8, 10)
odd = (1, 3, 5, 7, 9)
joinned_tuple_even_odd = even + odd
print(joinned_tuple_even_odd)