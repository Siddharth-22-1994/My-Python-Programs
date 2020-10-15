# from tkinter import *
# from tkinter import messagebox


# Button
# parent = Tk()
# redbutton = Button(parent, text='Left', fg='red', bgcolor='black')
# redbutton.pack(side=LEFT)

# greenbutton = Button(parent, text='Right', fg='green')
# greenbutton.pack(side=RIGHT)

# bluebutton = Button(parent, text='Top', fg='blue')
# bluebutton.pack(side=TOP)

# blackbutton = Button(parent, text='Bottom', fg='yellow')
# blackbutton.pack(side=BOTTOM)

# parent.mainloop()
# ------------------------------
# box = Tk()
# box.geometry('500x500')
# box.title('Pop Up')

# b = Button(box, text='Click me', fg='red')
# b.pack()


# box.mainloop()
# --------------------------------
# wind = Tk()
# wind.geometry('500x400')

# sub_button = Button(wind, text='Submit', fg='red',
#                     width=15, highlightbackground='red', padx=20, pady=25, activebackground='black')
# sub_button.pack()
# sub_button.place(x=20, y=30)
# sub_button.config()

# wind.mainloop()

# top = Tk()

# top.geometry('200x400')


# def fun():
#     messagebox.showinfo('Hello, Red Button Clicked')


# b1 = Button(top, text='red', command=fun, activeforeground='yellow',
#             activebackground='pink', pady=10)
# b1.pack(side=LEFT)

# b2 = Button(top, text='Blue', activeforeground='blue',
#             activebackground='pink', pady=10)
# b2.pack(side=RIGHT)

# b3 = Button(top, text='Black', activeforeground='black',
#             activebackground='pink', pady=10)
# b3.pack(side=TOP)

# b4 = Button(top, text='Green', activeforeground='green',
#             activebackground='pink', pady=10)
# b4.pack(side=BOTTOM)


# top.mainloop()

# d1 = {'a': 'se', 'b': 'ui', 'c': 'ty'}
# for val, val1 in d1.items():
#     print(val, ':', val1)

# x = 5

# print(a)
# y = 78


# def sum(a, b):
#  y = 9
#  print(x)
#  print(a+b)
#  print(y)


# sum(3, 4)
# print(y)

# if 0:
#     print('yes')
# else:
#     print('false')

# class profile:
#     def __init__(self, name, age):
#         self.fname = name
#         self.fage = age

#     def display(self):
#         print(self.fname, self.fage)


# p = profile('Sidhu', 26)

# setattr(p, 'fname', 'Siddharth')
# p.display()

# x = int(input())
# sum1 = 0
# while x != 0:
#     rem = x % 10
#     sum1 = sum1+rem
#     x = x/1
# print(sum1)

# a = int(input())
# rem = 0
# while a != 0:
#     i = a % 10
#     rem = rem+i
#     a = a/10
# print(int(rem))

# def prof():
#     fname = 'Sidhu'
#     sname = 'T'
#     d1 = {'a': fname, 'b': sname}
#     print(d1['a']+' '+d1['b'])


# prof()

# print('hello world')

# a = 2
# print(a)

# 1.) first letter should be an alphabet or underscore
# 2.) apart from 1st letter, next characters can be as alphabets(a-z), (A-Z), _, (0-9)
# 3.)(! @  # $ % ^ & *)
# 4.) not be a keyword
# 5.) case sensitive

# a = b = 8
# print(a)
# print(b)

# a, b = 9
# print(a)
# print(b)
# o/p
# Error

# a = 2, 3
# print(a)

# a, b, c = 2, 3
# print(a, b, c)

# a, b = c = 2, 3
# print(a)
# print(b)
# print(c)

# a = b, c = 4, 5
# print(a)
# print(b)
# print(c)

# import math
import copy
import math
a = 8
b = 5

# temp = a
# a = b
# b = temp

# print(a)
# print(b)

# a = a+b
# b = a-b
# a = a-b

# print(a)
# print(b)

# a = a*b
# b = a/b
# a = a/b

# print(int(a))
# print(int(b))

# a, b = b, a
# print(a)
# print(b)

# String
# numeric
# boolean
# None
# Collection Type

# a = 'Hello'
# print(a)

# b = 8
# c = 9.8
# d = 3+7j
# print(int(d))
# e = None
# print(type(e))

# list - -> [2, 3, 4, 5]
# tuple - -> ()
# set - -> {}
# # dict--> {key: value}

# Arithmatic
# Comparison
# Assignment
# Logical
# Bitwise
# Membership
# Identity

# Arithmatic
# +, -, *, /, %, **, //

# a = 27
# b = 2
# print(a % b)

# c = a**b
# print(c)

# print(int(math.pow(a, b)))

# Comparison
# ==, >, <, >=, <=, !=

# a = 4
# b = 5
# print(a != b)

# Assignment
# =, +=, -=, *=, %=, **=

# a %= 2
# print(a)

# Logical
# and, or, not

# print(not(a > 2 or a < 7))

# Bitwise
# &, |, ^, ~, <<, >>

# print(a | b)

# Membership operators
# in, not in
# x = 'Hello'
# print('e' not in x)

# y = [2, 3, 4, 5, 'io']
# print(5 in y)

# Identity Operator
# is, is not

# a = 9
# b = 9
# print(a is b)

# print(id(a))
# print(id(b))

# s1 = 'Hlo'
# s2 = 'hlo'
# print(s1 is s2)
# print(id(a))
# print(id(b))

# l1 = [2, 3, 4, 5]
# l2 = [2, 3, 4, 5]
# print(l1 is l2)

# Strings
# str1 = 'Hello How are you'

# dont have method to reverse
# print(str1)
# print(str1[-6:-1])
# print(len(str1))
# print(str1*4)
# print(str1.lower())
# print(str1.upper())
# print(str1.strip())
# print(str1.replace('H', 'z'))
# print('hello' not in str1)

# s1 = 'Hello'
# s2 = 'World'
# print(s1+' '+s2)

# name = 'Sidhu'
# age = 26

# print('My name is'+' '+name+'My age is'+' '+age)
# txt = 'My name is {}. Iam {} years old'
# print(txt.format(name, age))

# data types
# string
# numeric
# Boolean
# None

# numeric
# int
# float
# complex

# Collection datatypes
# List
# Tuple
# set
# Dictionary

# a = 0.9

# print(str(a))
# print(int(a))
# print(float(a))
# print(bool(a))
# print(complex(a))

# List
# l1 = [1, 2, 3, 4, 8, 2, 'Huji', 0.9, -78.09]

# list is ---> mutable
# ordered ---> indexed
# allow duplicate Items

# print(l1)
# print(l1[-8:-2])
# --------------------------

# a = 8
# print(a)

# a = b = 6
# print(a)
# print(b)

# a, b = 2, 3
# print(a, b)

# a, b = 7
# print(a)
# print(b)

# a = 9, 5
# print(a)

# a, b = c = 2, 4
# print(a)
# print(b)
# print(c)

# a = b, c = 1, 5
# print(a)
# print(b)
# print(c)

a = 9
b = 8

# temp = x =>9
# x = y =>8
# y = temp => 9

# print(x)
# print(y)

# a = a+b
# b = a-b
# a = a-b

# print(a)
# print(b)

# a, b = b, a
# print(a)
# print(b)

# Keywords
# Literals

# String
# numeric --> int, float, complex
# Boolean
# None
# Collection --> List, Set, Tuple, Dictionary

# a = 'hilo'
# print(type(a))
# b = 9
# print(type(b))

# c = True
# print(type(c))

# d = False
# print(type(d))

# e = None
# print(type(e))

# Operators

# Arithmatic
# Comparison
# Assigment
# Logical
# Bitwise
# Membership
# Identity

# Arithmatic
# +, -, *, /, %, **, //

# print(5 ** 3)

# print(int(math.gcd(12, 7)))

# Comparison
# ==, >, <, >=,<=, !=

# x = 17
# y = 7
# print(x > y)

# Assignment
# =, +=, -=, *=, /=, %=, **=

# a = 8
# a **= 2
# print(a)

# Bitwise
# &, | , ^ , ~, << , >>

# a = 8
# b = 6
# print(a | b)

# Logical
# and, or, not

# x = 9
# print(not(x > 2 or x < 7))

# Membership

# in, not in
# a = [1, 2, 3, 4, 5, 'H', -0.9]
# print('H' not in a)

# ------------------------------------------------ List
# l1 = [2, 3, 4, 5, 2, 9.8, 'po', -90, 2, 2]
# print(l1)
# print(l1[begining:ending:incremet])
# print(l1[1:9:2])
# print(l1[-6:-1])

# print(l1[::-1])
# l1.reverse()
# print(l1)

# replace element
# l1[2] = 'apple'
# print(l1)

# for val in l1:
#     print(val)

# print(len(l1))

# Add element to list
# append()
# insert()

# l1.append(987)--> The element will be added to the last position,
#                   only one element can be added at a time
# print(l1)

# l1.insert(4, 'car')
# print(l1)

# Remove element to list
# pop()
# remove()
# clear()
# del

# l1.pop(3) --> default it removes last element of list, use index vales to remove specific elements
# print(l1)

# l1.remove('po') --> Directly mention the element, that want to be removed
# print(l1)

# l1.clear() --> Empty the list
# print(l1)

# del l1[2]  # - ->   index
# print(l1)

# copy
# l2 = l1
# print(id(l1))
# print(id(l2))

# l2 = l1.copy()
# print(id(l2))
# print(id(l1))

# l2 = copy.copy(l1) --> Shallow copy
# print(l2)

# l2 = copy.deepcopy(l1) --> deep copy
# print(l2)

# l2 = list(l1)
# print(l2)

# concatination
# l1 = [2, 3, 4, 5, 2, 9.8, 'po', -90, 2, 2]
# l2 = ['cars', 'fruits', 'veg']
# print(type(l2))
# ans = l1+l2
# print(ans)

# extend()
# l1.extend(l2)
# print(l1)

# list constructor
# new = list(('apple', 'mango', 'grapes'))
# print(new)

# Tuple -------------------------------------
# ()

# majourly datatypes are divided to 2 catagories
# Basic datatypes
# Collection dataypes

# String
# numeric
# int
# float
# complex
# Boolean
# None

# b = 'hello'
# print(type(b))

# a = 23
# print(type(a))

# a = 23.7
# print(type(a))

# x = 2+8j
# print(type(x))

# d = False
# print(type(d))

# e = None
# print(type(e))

# a = name1
# b = name2
# c = name3

# 30 student --> 30 variables

# list --> []
# set
# tuple
# dictionary

l1 = [1, 90, 3, 4, 'name1', 'name2', 0.9, -78]
# print(l1)

# Index values to acess list
# postive , negative
# print(l1[-2])
# print(l1[1:9:3])

# length of element in list
# len()
# print(len(l1))

# To know the index value of element
# index()
# print(l1.index('name1'))

# reverse()
# l1.reverse()
# print(l1)

# Add element to this list
# append()
# insert()

# --> can add only one element at a time,
# added in the last position of the list
# l1.append('cars')
# print(l1)

# l1.insert(3, 'Apple')
# print(l1)

# Replace
# no methods for replacing
# l1[1] = '8678'
# print(l1)
