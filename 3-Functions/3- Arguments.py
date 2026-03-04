# ARBITRARY ARGUMENTS
def my_func(*fruit_list):
    return f"My fav fruit is {fruit_list[2]}"


res = my_func("Apple", "Banana", "Cherry", "Orange", "kiwi")
print(res)