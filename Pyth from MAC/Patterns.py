# # Patterns

# # To print Square

# for val in range(4):
#     for j in range(4):
#         print('*', end=' ')
#     print()

# # To Print Right angles Triangle

# for row in range(1, 6):
#     for val in range(row):
#         print('*', end='')
#     print()

# num = int(input())
# for i in range(1, num+1):
#     print('*' * i)

# num = int(input())
# for k in range(1, num):
#     print('*'*k, " "*(num-k))

# # Inverted right angled Triangle

# num = int(input())
# for k in range(1, num):
#     print(" "*(num-k), '*'*k)


# # To print Equalatral Triangle

# for i in range(1, num+1):
#     print(" "*(num-i)+" *"*i)

# # To Print Diamond

# num = int(input())
# for val in range(1, num+1):
#     print(" "*(num-val)+" *"*val)
# for val in range(num, 0, -1):
#     print(" "*(num-val)+" *"*val)

# # Printing num in right angles triangle shape

# for val in range(1, 6):
#     for val1 in range(val):
#         print(val, end=' ')
#     print()

# # printing name is right angles trinagle shape

# a = 'Vimal'
# for val in range(len(a)):
#     for val in range(val):
#         print(a[val], end='')
#     print()

# While loop
# Right angled triangle
i = 1
while i < 11:
    j = 0
    while j < i:
        print('*', end='')
        j = j+1
    print()
    i = i+1
print("Rest of the program")
