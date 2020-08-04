import random

l1 = []
finallist = []
for sm in range(ord('a'), ord('z')+1):
    l1.append(chr(sm))
ans = random.choice(l1)
finallist.append(ans)
# print(finallist)


# print(l1)
for bg in range(ord('A'), ord('Z')+1):
    l1.append(chr(bg))
ans1 = random.choice(l1)
finallist.append(ans1)
# print(finallist)

# print(l1)
for val in range(1, 101):
    l1.append(val)
ans2 = random.choice(l1)
finallist.append(ans2)
# print(finallist)

# print(l1)
spl = ['!', '@', '$', '%', '^', '&', '*', '_']
for ch in spl:
    l1.append(ch)
# print(l1)

i = 0
while i <= 6:
    ans4 = random.choice(l1)
    finallist.append(ans4)
    i = i+1
# print(finallist)

ans3 = random.choice(spl)
finallist.append(ans3)
# print(finallist)

for ans5 in finallist:
    print(ans5, end='')
# print(l1)

# print(l1)

# import random
# a = 'banana'
# print(random.choice(a))
