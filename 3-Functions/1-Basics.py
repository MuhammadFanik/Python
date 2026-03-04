def myfunc():
    print("Inside a function")

myfunc()


# RETURN A VALUE - If the function does not have any return statement, it returns None by default
def get_remainder(a, b):
    return a % b

ans = get_remainder(10, 4)
print(ans)
