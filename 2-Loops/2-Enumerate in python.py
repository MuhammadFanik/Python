# Enumerate - get both index and the element
a = ["Geeks", "for", "geeks"]
for i, name in enumerate(a):
    print(f"Index {i}: {name}")
# Converting to a list of tuples
print(list(enumerate(a)))
# Syntax --> enumerate(iterable, start=0)



# EXAMPLE USE CASES
# 1- ENUMERATING A DICTIONARY - We can get both, the index and it's key-value pair
d = {
    "a":10,
    "b":20,
    "c":30
}
for index, (key, value) in enumerate(d.items()):
    print(f"{index} - {key}:{value}")

print("\n")

# 2- Enumerate a string
s = "python"
for i, character in enumerate(s):
    print(i, character)