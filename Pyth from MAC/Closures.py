# Closures
#             Fisrt to know
# Nested Function and Functions are objects

# Eg1:
# Nested Function


def outer():
    z = 4

    def inner():
        print(z)
    inner()


outer()


# Eg: 2
# Function are objects

def add(a, b):
    c = a+b
    print(c)


a = add(2, 5)
a


# Eg=3
# Closures


def outer1():
    x = 3

    def inner1():
        y = 3
        res = x+y
        return res
    return inner1


a = outer1()
# To print answer
print(a())
# This helps to verify
print(a.__name__)
