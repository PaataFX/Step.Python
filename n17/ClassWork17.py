# #Public Protected Private
# class Car:
#     def __init__(self, model, year, price=0):
#         assert type(model) is str, "Enter string in model field"
#         assert year > 2000, "Old cars are not welcome"
#         assert price >= 0, "Price can not be negative!"
#         self.__model = model
#         self.year = year
#         self.price = price
#     @property
#     def model(self):
#         return self.__model
#     @model.setter
#     def model(self, value):
#         assert type(value) is str, "Enter string in model field"
#         self.__model = value
#     @model.getter
#     def model(self):
#         print("Trying to get model info")
#         return self.__model
#     @model.deleter
#     def model(self):
#         print("Trying to delete model")
#         del self.__model


# car1 = Car("BMW X6", 2001, 1000)
# del car1.model



# class Car2:
#     def __init__(self, price=0):
#         self.__model = "BMW"
#         self._year = 2000
#         self.price = price
#         self.greeting = "Hello"


# class Child_Car(Car2):
#     def __init__(self, price):
#         super().__init__(price)
#         print(self.__model)

# minicuper = Child_Car(1000)


# from abc import ABC, abstractmethod
# class MyABS(ABC):
#     @abstractmethod
#     def movement(self):
#         pass

#     @abstractmethod
#     def stopped(self):
#         pass

#     @abstractmethod
#     def charging(self):
#         pass

# class Not_Fully_Abstract(MyABS):
#     @staticmethod
#     def movement():
#         print("I am moving")

#     @staticmethod
#     def charging():
#         print("I am charging")

#     @staticmethod
#     def stopped():
#         print("I stopped")

# obj = Not_Fully_Abstract()










# class PyClass:
#     def find_correct_function(self, value):
#         if type(value) is str:
#             return self.__work_with_string(value)
#         if type(value) is int:
#             return self.__work_with_integer(value)

#     def __work_with_integer(self, value):
#         print(f"Working with integer {value}")

#     def __work_with_string(self, value):
#         print(f"Working with string {value}")

# obj = PyClass()
# obj.find_correct_function("a")
# obj.find_correct_function(1)



# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
        
#     def __call__(self):
#         print("Before function")
#         self.func()
#         print("After function")
# @MyDecorator        
# def function():
#     print("Main Function")
# function()




# class Descriptor:
#     def __get__(self, instance, owner):
#         print("Get Value")
#         return instance.value

#     def __set__(self, instance, value):
#         print("Set Value")
#         instance.value = value

#     def __delete__(self, instance):
#         print("Delete Value")
#         del instance.value

# class New_Class:
#     def __init__(self, value):
#         self.value = value
#     desc = Descriptor()

# new_obj = New_Class(20)

# # print(new_obj.desc)
# del new_obj.desc



