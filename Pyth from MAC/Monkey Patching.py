

# Monkey patching is a Dynamic modification of a class or a module at run time
# (i.e) We can change 3rd party code without changing the source code.

class test:
    def myfun(self):
        print('This is class method')


def fun():
    print('This is function')


test.myfun = fun

test.myfun()
