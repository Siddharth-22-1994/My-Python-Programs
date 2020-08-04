class profile1:
    name = input()
    age = int(input())
    password = input()
    conf_pass = input()
    address = input()


p = profile1()
assert p.password == p.conf_pass, 'Password mismatching'

assert getattr(p, 'address') == ('Hydrabad') or getattr(
    p, 'address') == ('Telagana'), 'Please, enter in your city website'


class address:
    address = input()

    def conf_address(self):
        return self.address


a = address()
a.conf_address()

assert getattr(p, 'address') == getattr(a, 'address'), 'Address mismatch'
print('You have registered')

print(p.name, p.age, p.password, p.conf_pass, p.address)
print(getattr(a, 'address'))
