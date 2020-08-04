# Meth:1

l1 = [2, 3, 4, 5, 6]
l1size = len(l1)
temp = l1[0]
# print(temp)
l1[0] = l1[l1size-1]
l1[l1size-1] = temp

print(l1)


# Meth:2

l1 = ['w', 'r', 'u', 'i', 'o']
l1[0], l1[-1] = l1[-1], l1[0]
print(l1)
