import datetime
name = str(input())
age = int(input())

bal = 100-age

x = datetime.datetime.now()
year = x.year
ans = year+bal
print('Your 100th age will be', ans)
