class Person:
    def say_hi(self):
        print('Hello,How are you?')


p = Person()
p.say_hi()

# Above statements can also be written as:
Person().say_hi()
print(' ')


class Parrot:
    def fly(self):
        print("Parrot can fly")


class Penguin:
    def fly(self):
        print("Penguin can't fly")


blu = Parrot()
peggy = Penguin()

blu.fly()   # fly function of Parrot class accessed
peggy.fly()  # fly function of Penguin class accessed
