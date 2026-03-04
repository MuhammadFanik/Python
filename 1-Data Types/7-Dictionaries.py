# ORDERED, CHANGEABLE, AND DO NOT ALLOW DUPLICATES
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["model"])
# Length of dictionary
print(len(thisdict))
# Type of dictionary
print(type(thisdict))


# ACCESS DICTIONARY ITEMS
# Accessing Items
print(thisdict["year"])
# Get Keys - keys() method will return a list of all the keys in the dictionary
print(thisdict.keys())
# Get Values - Values() method will return a list of all the values in the dictionary
print(thisdict.values())
# Get Items - Items() method will return each item in a dictionary, as tuples in a list
print(thisdict.items())
# Check if key exists in dictionary
print("car_name" in thisdict)


# CHANGE DICTIONARY ITEMS
thisdict["year"] = 2020
print(thisdict)


# ADDING ITEMS
thisdict["owner"] = "First owner"
print(thisdict)
print("\n\n")

# LOOP DICTIONARIES - When looping through a dictionary,
# the return value are the keys of the dictionary, but there are methods to return the values as well
for x in thisdict:  # Prints all the key names in dictionary, one by one
    print(x)

for x in thisdict.values(): # Returns the values of a dictionary
    print(x)

for x, y in thisdict.items():
    print(x, y)


# COPY DICTIONARIES
# You cannot copy a dictionary by typing dict1 = dict2 because dict2 will be a reference to dict1,
# and any changes made to dict2 will be reflected in dict1.
# Instead, use the copy method