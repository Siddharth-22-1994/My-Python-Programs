# Lambda inside List

math = [lambda a: a+2, lambda a:a-2, lambda a:a*2, lambda a:a/2]

for val in math:
    print(val(6))

# Dict inside List

math = {'add': lambda a: a+2,
        'sub': lambda a: a-2,
        'mul': lambda a: a*2,
        'div': lambda a: a/2
        }
x = math['add'](4)
print(x)
