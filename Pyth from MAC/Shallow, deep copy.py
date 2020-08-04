import copy

# Shallow
a = [[1, 2, 3], [5, 6, 7], [4, 3, 2]]
l1 = copy.copy(a)
a[1][0] = 'E'
print(l1)
print(a)
print(id(a), 'a')
print(id(l1), 'l1')

# Deep
# a = [[1, 2, 3], [5, 6, 7], [4, 3, 2]]
l2 = copy.deepcopy(a)
a[1][0] = 'U'
print(l2)
print(a)
print(id(a), 'a')
print(id(l2), 'l2')
