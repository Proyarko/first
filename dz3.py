
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hapiness = 100
        self.sadness = 0

class Student(Person):
    def __init__(self, knoghledge, free_time):
        super(). __init__(self)
        self.knoghledge = knoghledge
        self.free_time = free_time

class Adult(Person):
    def __init__(self, money, knoghledge):
        super().__init__(self)
        self.knoghledge = knoghledge
        self.money = money
