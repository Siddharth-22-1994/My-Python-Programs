print('Press 1 to View People\nPress 2 to Add People\nPress 3 to Add Phone')

n = int(input())

a = '1. People view'
b = '2. Add Peolple'
c = '3. Add Phone'
d = 'Update name'
e = 'Update Phoen'

if n == 1:
    view_people = open('Tele_directry.txt', 'r')
    ans = view_people.read()
    print(ans)

elif n == 2:
    i = 0
    i = i+1
    ans = str(i)
    print('Enter you name')
    name = input()
    print('Enter Phone Number')
    Phone = str(input())
    lenphone = len(Phone)
    if lenphone == 10:
        d1 = {'Name': name, 'Phone': Phone}
        for val, val1 in d1.items():
            store = val, val1
            str_store = str(store)

            store_to_file = open('Tele_directry.txt', 'a')
            print('\n{}{}'.format(ans, store_to_file.write(str_store)))
    else:
        print('Enter Valid Phone Number')
