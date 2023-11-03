# class Car:
#     def __init__(self, speed, model, weight):
#         self.speed = speed
#         self.model = model
#         self.weight = weight
#         self.passenger = []
#     def addpassenger(self, passenger):
#         self.passenger.append(passenger)
#     def showpassenger(self):
#         for i in self.passenger:
#             print(i.name)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Bob = Person('Bob', 45)
# jack = Person('Jack', 35)
# car = Car(200, 'Mers', 2000)
# car.addpassenger(Bob)
# car.addpassenger(jack)
# car.showpassenger()





# class Human:
#     def __init__(self, name, age, money, tiredness, happiness):
#         self.name = name
#         self.age = age
#         self.money = 0
#         self.tiredness = 0
#         self.happiness = 100
#         self.job = None
#         self.house = None
#         self.car = None
#     def Work(self):
#         self.money += 100
#         self.happiness += 75
#     def Buy_car(self, car):
#         if self.money >= car.price:
#             self.car = car
#         else:
#             print('go work')
#     def Buy_house(self, house):
#         if self.money >= house.price:
#             self.house = house
#         else:
#             print('go work')
#     def get_job(self, job):
#         self.job = job
#
# class car:
#     def __init__(self, speed, model):
#         self.speed = speed
#         self.model = model
# class house:
#     def __init__(self, status):
#         self.status = status
#         self.furnitur = []
#         self.people = []
# class Job:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary




# class Person:
#     def __init__(self, name, hapiness, age, money):
#         self.name = name
#         self.hapiness = 100
#         self.age = age
#         self.money = money


# class Student(Person):
#     def __init__(self, knoghledge, free_time):
#         super(). __init__(self)
#         self.knoghledge = knoghledge
#         self.free_time = free_time



# class squaer:
#     def __init__(self,side):
#         self.side = side

#     def s(self):
#         return self.side ** 2 
# class rectangle(squaer):
#     def __init__(self, side2):
#         super().__init__(self)
#         self.side2 = side2
#     def S2(self):
#         return self.side2 * self.side

# squae = squaer(10)