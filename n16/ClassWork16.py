# # creating class example
# class car:
#     #attribute
#     wheels = 4
#     #creating method
#     @staticmethod
#     def movement():
#         print("car is moving!")
# #access to class attributes
# (car.movement())

# #5 human attribute and 4 methods
# class Humans:
#     hands = 2
#     legs = 2
#     eyes = 2
#     ears = 2
#     mouth = 1
#     nose = 1
#     @staticmethod
#     def walking():
#         print("human is walking!")
#     def talking():
#         print("human is talking!")
#     def sleeping():
#         print("human is sleeping!")
#     def running():
#         print("human is running!")
# (Humans.walking())


# class Car:
#     wheels = 4
#     @staticmethod
#     def movement():
#         print("car is moving!")
#     def stop():
#         print("car is stopped!")
# car1 = Car
# car2 = Car
# Car.wheels = 3
# print(car1.wheels)
# print(car2.wheels)

# class Car:
#     wheels = 4
#     @staticmethod
#     def movement():
#         print("car is moving!")
#     def stop():
#         print("car is stopped!")
# car1 = Car
# car2 = Car
# car1.name = "BMW"
# print(car1.name)


# class Car:
#     #class attribute
#     attr1 = "Four Wheeled Car"
#     def __init__(self,name):
#         #initiation attribute
#         self.name = name
# class Human:
#     hands = 2
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#     def greetings(self):
#         print(f"Hello, my name is {self.name}")
#     @classmethod
#     def hands_number(cls):
#         print(f"Hello, I have {cls.hands} hands")
#     @staticmethod
#     def talking():
#         print("Bla Bla Bla")
#     def __repr__(self):
#         return f"Human: ('{self.name}', '{self.lastname}', '{self.age}')"
# class Georgian(Human):
#     hero = "Tamada"
#     problems = True
#     occupied = "By Russia"
#     georgian = "European"
    
#     def drinking(cls):
#         print(f"{cls.name} {cls.lastname} {cls.hero} is drinking")
# georgian_hero = Georgian("Kartveli", "Vajkaci", "30-60")
# georgian_hero.drinking()


# #parental class
# class Car:
#     Wheels = 4
    
#     @staticmethod
#     def moving():
#         print("car is moving")
# #child class
# class BMW(Car):
#     brand = "BMW"
    
#     def drifting(cls):
#         print("f{cls.brand} is drifting")

# BMW.moving()
# BMW.drifting()


