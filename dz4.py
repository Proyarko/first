class Human:
    def __init__(self, name, age, money, tiredness, happiness):
        self.name = name
        self.age = age
        self.money = 0
        self.tiredness = 0
        self.happiness = 100
        self.job = None
        self.house = None
        self.car = None
class Car:
    def __init__(self, speed, model):
        self.speed = speed
        self.model = model
class House:
    def __init__(self, status):
        self.status = status
        self.furnitur = []
        self.people = []
class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Life(Human, Car, House, Job):
    def __init__(self):
        super().__init__(self)
        
