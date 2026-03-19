# The enclosing namespace exists in nested functions. It's the namespace of the outer function.
# The simple idea is that if a variable is not in local scope, or global scope, it looks in the outer function

def outer():
    x = "enclosing"
    def inner():
        print(x)

    inner()

outer()

# inner() cannot find "x" locally, so it looks in the enclosing namespace (outer function)