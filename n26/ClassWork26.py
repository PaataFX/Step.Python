# SOLID 
# 1. Single-responsibility principle (SRP)
# 2. Open–closed principle (OCP)
# 3. Liskov substitution principle (LSP)
# 4. Interface segregation principle (ISP)
# 5. Dependency inversion principle (DIP)



# # 1. Single-responsibility principle (SRP)

# #Incorrect
# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def send_email(self, message):
#         pass

#     def place_order(self, order):
#         pass

#     def generate_invoice(self, invoice):
#         pass

#     def add_feedback(self, feedback):
#         pass

# #Correct
# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

# class EmailService:
#     def send_email(self, customer, message):
#         print(f"{customer.name} have sent message '{message}' by email {customer.email}" )

# class Order:
#     def place_order(self, customer, order):
#         pass

# class Invoice:
#     def generate_invoice(self, customer, invoice):
#         pass

# class Feedback:
#     def add_feedback(self, feedback):
#         pass

# customer1 = Customer("Nika", "nika@gmail.com")

# email_service_obj = EmailService()

# email_service_obj.send_email(customer1, "Hello World!")


#2 Open-Closed Principle

# #Correct
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# a  = Circle(15)
# print(a.area())

# #3 The Liskov Substitution Principle
# #შვილობილმა კლასმა უნდა გააფართოოს მშობლის შესაძლებლობები და არასოდეს დაავიწროოს

# #incorrect

# # class KitchenApp:
# #     def on(self):
# #         pass
# #     
# #     def off(self):
# #         pass
# #     
# #     def set_temperature(self, value):
# #         pass
# # 
# # class Toster(KitchenApp):
# #     def on(self):
# #         print("Toster is On")
# #     
# #     def off(self):
# #         print("Toster is Off")
# #     
# #     def set_temperature(self, value):
# #         print(f"Temperature is set to {value}")
# #         
# # class Juicer(KitchenApp):
# #     def on(self):
# #         print("Juicer is On")
# # 
# #     def off(self):
# #         print("Juicer is Off")

# #Correct

# class KitchenApp:
#     def on(self):
#         pass
#     def off(self):
#         pass
    
# class Juicer(KitchenApp):
#     def on(self):
#         print("Juicer is On")

#     def off(self):
#         print("Juicer is Off")
        
# class KitchenAppWithTemp(KitchenApp):
#     def set_temperature(self, value):
#         pass

# class Toster(KitchenAppWithTemp):
#     def on(self):
#         print("Toster is On")

#     def off(self):
#         print("Toster is Off")

#     def set_temperature(self, value):
#         print(f"Temperature is set to {value}")

# #4 Interface Segregation Principle

# #Correct
# class Printing:
#     def print(self):
#         pass

# class Scanning:
#     def scan(self):
#         pass

# class Printing_Device(Printing):
#     def print(self):
#         print("Printing document!")
        
# class Multifunctional_Printer(Printing, Scanning):
#     def print(self):
#         print("Printing document!")

#     def scan(self):
#         print("Scanning document!") 


# # 5. Dependency inversion principle (DIP)

# #correct

# from abc import ABC, abstractmethod

# class LoggerInterface(ABC):
#     @abstractmethod
#     def log(self, message):
#         pass


# class Logger(LoggerInterface):
#     def log(self, message):
#         with open("log.txt", "a") as file:
#             file.write(message + "\n")

# class Calculator:
#     def __init__(self, logger: LoggerInterface):
#         self.logger = logger


#     def add(self, x, y):
#         result = x + y
#         self.logger.log(message=f"{x} + {y} = {result}")
#         return result


# calculator1 = Calculator(Logger())
# calculator1.add(5, 7)

