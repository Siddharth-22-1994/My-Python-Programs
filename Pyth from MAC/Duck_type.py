# Conceptual type example

# Eg:1

# class original:
#     def duck(self):
#         print('This is duc typing')


# class orig2:
#     def duck(self):
#         print('Orig2 class')


# class display:
#     def exec(self, ide):
#         ide.duck()


# o = orig2()

# d = display()
# d.exec(o)

# Eg:2
# class duck:
#     def quack(self):
#         print('The duck is quacking')


# class Monkey:
#     def quack(self):
#         print('The monkey also qucking')


# def disp(obj):
#     obj.quack()


# d = Monkey()
# disp(d)


# Real time example

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


for val in MyRange(1, 10):
    print(val)
