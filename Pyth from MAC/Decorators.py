# Decorators

# 1. Basics to know decorators, we have to know

# Name Spaces
# Variable scopes
# Closures
# Decorators

# 2. To know about decorators
# Nested Functions
# Function return function
# reference
# function as a parameter of another function


# On sub dividing decorators


# Decorators applied to a class
# a function
# to a classmethod
# to a instancemethod
# Universal decorators
# Synchronised Decorators(Decorators in multi-Threading)

# 1st step
# Function as a parameter to anotherfunction

# def func1():
#     print('This is function1')


# def function2(func):
#     print('This is finction2')
#     func()


# function2(func1)


# Decorator
# Eg:1

def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


@str_upper
def greet():
    return 'good morning'


print(greet())

# 1st method to print decorated text
# d = str_upper(greet)
# print(d())

# Eg:2


def decor(func):
    def inner(x, y):
        if y == 0:
            print('Give proper input')
        return func(x, y)
    return inner


@decor
def div(a, b):
    return a/b


print(div(4, 0))

# Eg:3


def decfun(func):
    def innerfun(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)
    return innerfun


@decfun
def subr(a, b):
    c = a-b
    return c


a = int(input())
b = int(input())

print(subr(a, b))

# Eg:4
# Add and sub Interchange example

a = int(input())
b = int(input())


def decofun(func):
    def add(x, y):
        return x+y
        return func(x, y)
    return add


@decofun
def subr(a, b):
    c = a-b
    return c


print(subr(a, b))
