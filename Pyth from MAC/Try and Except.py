# Value error
# ValueError is raised when a function receives an argument of the
# correct type but an inappropriate value.

# Eg1
import math

x = int(input())
try:
    ans = math.sqrt(x)
    print(ans)
except Exception:
    print('Enter Positive number')
    print('Hello')

# Zerodivision Error
# ZeroDivisionError: Occurs when a number is divided by zero.

# Eg1:
try:
    a = 2
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Plaese give proper input')
