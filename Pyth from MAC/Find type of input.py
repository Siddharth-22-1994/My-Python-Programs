a = eval(input())
try:
    b = a.real
    if b:
        print('The given datatype is complex')
except:
    if a.isnumeric():
        print('The given num is Integer type')
    elif a.isalpha():
        print('The input is string type')
    elif float(a):
        print('The given input is float type')
        try:
            if bool(a):
                print('This is bool type')
        except:
            print('Code completed')
