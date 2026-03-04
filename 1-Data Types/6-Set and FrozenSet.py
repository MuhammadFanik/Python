# SET IS UNORDERED, UNCHANGEABLE, and UNINDEXED
# UNCHANGEABLE, BUT YOU CAN REMOVE OR ADD NEW ITEMS
# DOES NOT ALLOW DUPLICATES
# THE VALUE TRUE AND 1 ARE CONSIDERED SAME IN SETS AND TREATED AS DUPLICATES. SAME FOR FALSE AND 0
# SET ITEMS CAN BE OF ANY DATA TYPE and THEY CAN CONTAIN MULTIPLE DATA TYPES AS WELL

myset = {"cinnamon", "cardamom", "red chilli"}
print(myset)

# Length of set
print(len(myset))


# ACCESS SET ITEMS - You cannot access set items by referring to an index or key
# But you can loop through the set items using for loop or ask if a specified value is present in the set using the in keyword

num_set = {2, 4, 6, 8, False}
for number in num_set:
    print(number)

print(0 in num_set)


# ADD NEW SET ITEMS
names = {"Ali", "Ahmad", "Usman", "Umar", "Sulaiman", "Janhvi"}
# To add one item to a set, use the add() method
names.add("Shahid")
print(names)
# To add items from another set into the current set, use the update() method. The object in the update() method can be any iterable


# REMOVE SET ITEMS
# To remove an item from the set, use:
# 1- Remove() --> If the item to remove does not exist, this will raise an error
# 2- Discard() --> If the item to remove does not exist , this will not raise an error

# Pop method removes a random item from the set
# Clear method empties the set
# Del keyword will delete the set completely



# JOIN SETS
# 1- The union() and update() methods joins all the items from both sets
# 2- The intersection method only keeps the duplicates
# 3- The difference method keeps the items from the first set and that are not in the other set(s)
# 4- The symmetric_difference() keeps all items EXCEPT the duplicates

# Union - Returns a new set with items from both sets. It also allows you to join a set with other data types, like lists or tuples
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


# FROZENSET - Immutable version of a set. It also contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset
x = frozenset({"a", "b", "c"})
print(type(x))