# Syntax --> zip(*iterables)



# This example shows how zip function works when no parameter, one, and two iterables are passed as parameters
a = [1, 2, 3]
b = ["a", "b", "c"]

# No iterable passed
res1 = zip()
print(f"Res1: {tuple(res1)}")

# Only one iterable is passed
res2 = zip(a)
print(f"Res2: {tuple(res2)}")

# Two iterables are passed
res3 = zip(a, b)
print(f"Res3: {tuple(res3)}")

print("\n\n")
names = ["John", "Ali", "Sam", "Harris"]
scores = [70, 80, 90, 100]

res4 = list(zip(names, scores))
print(res4)