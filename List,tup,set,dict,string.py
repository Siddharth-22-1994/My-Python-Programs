Strings

a = 'siddharth, hello'
print(a.capitalize())
print(a.title())
print(a.upper())
print(a.lower())
print(a.replace('s', 'z'))

s = "My name is \"Siddharth\" "
print(s)

name = 'myname'
age = 24
place = 'coimbatore'
txt = 'My name is {}, Iam {} years old, Iam from {}'
print(txt.format(name, age, place))

from string import Template

txt = Template('My name is $name, Iam $age years old')
print(txt.substitute(name='myname', age=26))

-------------------------------------------------------------------------
List

l1 = ['2', '3', '4', '5', '6']
l3 = ['we', 'ui', 'op']

l1[2] = 'Apple'
print(l1)

print(len(l1))
print(max(l1))
print(min(l1))
l1.reverse()
print(l1)
a = l1.index('2')
print(a)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

import copy
l1 = [1, 2, 3, 4]
l2 = copy.deepcopy(l1)
l2[1] = 'Tiger'

print(l1)

print(l2)


# Add
l1.append('Orange')
print(l1)
l1.insert(2, 'grapes')
print(l1)

# Remove
l1.pop(2)
print(l1)

l1.remove('3')
print(l1)

# l1.clear()
# print(l1)

# del l1[0]
# print(l1)

# Copy
l2 = list(l1)
print(id(l1))
print(id(l2))

l2 = l1.copy()
print(id(l1))
print(id(l2))

import copy
l2 = copy.copy(l1)
print(l2)

l2 = copy.deepcopy(l1)
print(l2)

# Concatinate
ans = l1+l3
print(ans)

l1.extend(l3)
print(l1)

for val in l3:
    l1.append(val)
print(l1)

thislist = list((2, 4, 5, 6, 'gy', 'jh'))
print(thislist)

# Nested List
l2 = [12, 23, ['op', 'nm', [9, 0, 8], 98, 134], 78, 'g']
print(l2)

print(l2[2][1])

for z in l2:
    print(z)
--------------------------------------------------------
Tuple

a = 2
print(type(a))
b = 3,
print(type(b))
c = (12)
print(type(c))
d = (12,)
print(type(d))

t1 = (1, 2, 3, 4)
t2 = ('w', 's', 'u')
print(t1)

# print(t1[4][0])

print('we' in t1)

if 1 in t1:
    print('yes')


print(2 not in t1)

print(len(t1))
print(min(t1))
print(max(t1))

ans = t1.index(3)
print(ans)

# del t1
# print(t1)

t3 = t1+t2
print(t3)

tup = tuple(('d', 'i', 'p', 6, 9))
print(tup)
-----------------------------------------------------------
Set

s1 = {}
print(type(s1))

s1 = {1, 2, 3, 2}
print(s1)

s2 = {(3, 4), 'i', 'r', 2, 1}
s3 = [12, 23]
print(s2)

for val in s1:
    print(val)

print(2 in s1)

print(len(s1))
print(min(s1))
print(max(s1))

# Add
s1.add('er')
print(s1)

s1.update({10, 23, 89})
s1.update([10, 23, 89])
s1.update((10, 23, 89))
s1.update({2: 'we', 4: 45})
print(s1)

# Remove
# s1.pop()
# print(s1)

s1.remove(3)
print(s1)

s1.discard(289)
print(s1)

# del s1
# print(s1)

# s1.clear()
# print(s1)

Join
x = s1.union(s3)
y = s1.union(s2)
print(x)
print(y)

ans = s1.difference(s2)
print(ans)

ans3 = s2.difference(s1)
print(ans3)

ans1 = s1.intersection(s2)
print(ans1)

ans2 = s1.symmetric_difference(s2)
print(ans2)

setcons = set(('apple', 'mango', 'grapes'))
print(setcons)
-------------------------------------------------------------

dict
d1 = {1: 'a', 2: 'b', 3: 'c'}
print(d1)
print(d1[2])
print(d1.get(1))

d2 = {2+3j: '12', True: 'Yes', 9.8: 12, 3: 'p', 'ui': 89, (12, 90): ['12']}
print(d2)

# d3 = {{1: '23'}: 34}
# print(d3)

d4 = {1: 23, 1: 'er', 3: 'op'}
print(d4)

# replace Item using Keys
d1[2] = 'yu'
print(d1)

# loop though
for val in d1.values():
    print(val)

for val1 in d1.keys():
    print(val1)

for x, y in d1.items():
    print(x, y)

print(len(d1))

# Add items
d1[4] = 'd'
print(d1)


# Remove
d1.pop(1)
print(d1)

d1.popitem()
print(d1)

# del d1
# print(d1)

print(d1.clear())
print(d1)

# Nested Dict

mydict = {
    'c1': {
        'name': 'N1',
        'age': 10
    },
    'c2': {
        'name': 'N2',
        'age': 14
    },
    'c3': {
        'name': 'N3',
        'age': 15
    }
}
print(mydict)

# Constructor
thisdict = dict(fname='name1', age='25', place='place1')
print(thisdict)

formkeys
x = ('key1', 'key2', 'key3')
y = [4, 8]
ans = dict.fromkeys(x, y)
ans = dict.fromkeys(y, x)
print(ans)
