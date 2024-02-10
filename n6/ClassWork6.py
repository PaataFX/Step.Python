##### more about functions

# def new_func(a):
#     print(a)
# new_func(3)

# def new_function(a, b, c, d):
#     print(a, b, c, d)
#     return a
# new_function(1, 2, 3, 4)

# x = [1, 2, 3, 4]
# def new_function(a, b, c, d):
#     print(a, b, c, d)
#     return a
# new_function(*x)

# x = ["john", "doe"]
# def new_function(first="someone", last="someone", age=27):
#     print(f"""
#     Name: {first}
#     Lastname: {last}
#     Age: {age}
#     """)
# new_function(*x)

# x = ["john", "doe", "23"]
# def func():
#     # x = 7
#     print (x)
# # print(x)
# func()


# x=9 #global
# def func():
#     # x=7 #enclosed
#     print(x)
#     def func2():
#         # x = 3 #local
#         print(x)
#     func2()
# func()

# #1
# def func(a, b):
#     return a + b
# # print(func(5, 7))
# # a = func
# # print(a(5,7))

# # a = func
# # del func
# # print(a(2,3))


# #2
# def add(num1, num2):
#     return num1 + num2
# def malt(num1, num2):
#     return num1 * num2
# def process_func(my_func, num1, num2):
#     result = my_func(num1, num2)
#     return result
# print(process_func(malt, 3, 5))

# #3
# def make_circle_area(pi = 3.14):
#     def circle_area(r):
#         area = pi * r**2
#         return area
#     return circle_area
# f = make_circle_area()
# print(f(2))

# #4
# def square(num):
#     return num ** 2
# def cube(num):
#     return num ** 3
# def root(num):
#     return num ** (1/2)
# func_list = [square, cube, root]
# for func in func_list:
#     for i in range(1, 6):
#         print(func.__name__, i, "=", func(i))
#     print("___________________")

# #5
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         print(x)
#         return (x * factorial(x-1))
# print(factorial(9))

# def sum_all(*args):
#     sum_1 = 0
#     for arg in args:
#         sum_1 += arg
#     return sum_1
# print(sum_all(1,2,3,4,5,6,7,8,9,)) # * turns arguments into tuple

# def malt(*args):
#     sum_1 = 1
#     for arg in args:
#         sum_1 *= arg
#     return sum_1
# print(malt(2,5,5))

# def histogram(*args):
#     x = 0
#     for i in args:
#         for arg in i:
#             x += arg
#             print("*"*x)
#             x = 0
# histogram([4, 9, 7])

# def word_list(*words):
#     long_word = ""
#     for word in words:
#         if len(word) > len(long_word):
#             long_word = word
#     print(long_word)
# word_list("apple", "banana", "orange", "pineapple", "peach")

# def looper(num):
#     print("hi "*num)
# looper(19)

# def looper(num):
#     if num == 0: return
#     print("hi")
#     return looper(num - 1)
# looper(3)

# import time
# a = (time.time())
# i=3600000
# while i >0:
#     i -= 1
# b = (time.time())
# print(b-a)