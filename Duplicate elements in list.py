# Method: 1
# l1 = [2, 3, 4, 5, 2, 3]
# l1.sort()
# for i in range(len(l1) - 1):
#     if l1[i] == l1[i+1]:
#         print(l1[i])

# # Method :2  ---> Easy
# a = [1, 2, 3, 4, 2, 3, 6]
# for val in range(len(a)):
#     for val1 in range(val+1, len(a)):
#         if a[val] == a[val1]:
#             print(a[val1])

# Sorting of Dictionar based on values
d1 = {'a': 10, 'b': 9, 'c': -8, 'd': 100, 'e': 0}
print(sorted(d1.items(), key=lambda x: x[1]))
