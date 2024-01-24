######## პირობითი ოპერატორები ########

# # print(type(True))
# # print(type(False))
# # will print type bool

# # Python Assignment Operators
# # Operator	Example	    Same As
# # =	        x = 5	    x = 5	
# # +=	    x += 3	    x = x + 3	
# # -=	    x -= 3	    x = x - 3	
# # *=	    x *= 3	    x = x * 3	
# # /=	    x /= 3	    x = x / 3	
# # %=	    x %= 3	    x = x % 3	
# # //=	    x //= 3	    x = x // 3	
# # **=	    x **= 3	    x = x ** 3	
# # &=	    x &= 3	    x = x & 3	
# # |=	    x |= 3	    x = x | 3	
# # ^=	    x ^= 3	    x = x ^ 3	
# # >>=	    x >>= 3	    x = x >> 3	
# # <<=	    x <<= 3	    x = x << 3

# # Python Comparison Operators
# # Operator	Name	            Example
# # ==   Equal	                x == y	
# # !=   Not equal	            x != y	
# # >	   Greater than             x > y	
# # <	   Less than	            x < y	
# # >=   Greater than or equal to	x >= y	
# # <=   Less than or equal to	x <= y

# print(4<7)
# # will print: True

# print(4==7)
# # will print: False

# correct_user = "admin"
# correct_password = "1234"
# user = input("Enter your username: ")
# password = input("Enter your password: ")
# print(user == correct_user and password == correct_password)
# # will print: True

# # Code that checks if the password and the user is true. if true "welcome" if false ...
# correct_user = "admin"
# correct_password = "1234"
# user = input("Enter your username: ")
# password = input("Enter your password: ")
# if user == correct_user and password == correct_password:
#     print("Welcome")
# else:
#     print("Invalid username or password")


# name = input("Enter name: ").lower()
# if name=="bond":
#     print("Welcome on board 007")
# else:
#     print(f"good morning {name}")


# Name = (input("what's your name: "))
# age = int(input("what's your age: "))
# if age >= 18:
#     print(f"Welcome {Name}")
# else:
#     print("forbidden")


# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))
#
# if num1 <= num2 and num1 <= num3:
#     print(num1)
# elif num2 <= num3 and num2 <= num1:
#     print(num2)
# else:
#     print(num3)



# grade = int(input("Enter grade:"))
# if grade >= 91:
#     print("A")
# elif grade >= 81:
#     print("B")
# elif grade >= 71:
#     print("C")
# elif grade >= 61:
#     print("D")
# elif grade >= 51:
#     print("E")
# else:
#     print("F")



# user = input("username: ")
# password = input("password: ")
# if len(user) > 0 and len(password) <= 8:
#     print("you are registered!")
#     answer = input("do you want to login? yes/no: ")
#     if answer.lower() == "yes":
#         user1 = input("username: ")
#         password1 = input("password: ")
#         if user1 == user and password1 == password:
#             print("you are logged in!")
#         else:
#             print("wrong password or username")
#     else:
#         print(f"have a good day {user}")
# else:
#     print("you are not registered! User is empty or password is too short")




# population = int(input("Population in country: "))
# needed_antidote_number = population * 2
# reserves = int(input("Number of antidotes in reserve: "))
# if needed_antidote_number == reserves:
#     print("We can't do anything")
# elif needed_antidote_number > reserves:
#     print(f"Ask other country for {needed_antidote_number - reserves} units of antidote")
# else:
#     print(f"We can help other country with {reserves - needed_antidote_number} units of antidote")


# salary = int(input("What's your salary: "))
# years_of_work = int(input("How many years do you work here: "))
# taxes = (salary * years_of_work)*0.26

# print(f"""
# Salary over the years: {salary * years_of_work}
# Taxes over the years: {taxes}
# """)


# liters = int(input("How many liters of gasoline do yoy have: "))
# liters_for_km = liters/12
# city1 = "Zaragoza (50km) "
# city2 = "Valencia (75km) "
# city3 = "Madrid (100km) "
# if liters_for_km < 50:
#     print("!Emergency Landing")
# if liters_for_km >= 50:
#     print(f"You can go to {city1}", end="")
# if liters_for_km >= 75:
#     print(f"Or {city2}", end="")
# if liters_for_km >= 100:
#     print(f"Or {city3}", end="")
# print("airport to land")