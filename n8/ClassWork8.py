# def sum_all(some_list, i, n, count):
#     if n <= i:
#         return count
    
#     count += some_list[i]
    
#     count = sum_all(some_list, i+1, n, count)
    
#     return count

# list1 = [1,2,3,4,5]
# count = 0
# n = len(list1)
# print(sum_all(list1, 0, n, count))



# fruits = ["apple", "orange", "banana", "mango", "cherry"]
# new_list = []

# for x in fruits:
#     if "a" in x:
#         new_list.append(x)
# print(new_list)
# # is the same as
# new_list = [x for x in fruits if "a" in x]
# print(new_list)


# x = lambda a: a+5
# print(x(4))

# x = lambda a, b, c: a+ b + c
# print(x(4, 1, 2))

# def new_function (n):
#     return lambda a: a * n
# double = new_function(2)
# triple = new_function(3)
# print(double(3))
# print(triple(3))

# # new_list = [x for x in fruits]
# new2 = [lambda arg=x: arg*10 for x in range (10)]
# for fun in new2:
#     print(fun())

# malt_table = [lambda arg1=x, arg2=y: arg1*arg2 for x in range(1,11) for y in range(1,11)]
# for i, fun in enumerate(malt_table):
#     if i % 10 == 0:
#         print()
#     print(fun(), end=' ')
# # is the same as
# i = 0
# def malt(func_list):
#     global i
#     if i % 10 == 0  and i!=0:
#         print()
#     print(func_list[i](), end=" ")
#     if i < len(func_list) - 1:
#         i += 1
#         malt(func_list)
# malt(malt_table)

# max = lambda a, b: a if a> b else b
# print(max(3, 9))

# num = lambda a: "Is Number!" if a.isdigit() else "Is Not Number"
# print(num("1234"))
# print(num("something"))

# from functools import partial
# def pow(a, b):
#     return a**b
# pow2 = partial(pow, b=2)
# print(pow(2,4))
# print(pow2(2))


# from functools import reduce
# list1 = [1, 2, 3, 4, 5, 6]

# # sum_of_list = reduce(lambda a,b: a+b, list1) #reduce needs only two arguments
# # print(sum_of_list)
# # print(sum(list1))

# # max_el = reduce(lambda a,b: a if a > b else b, list1)
# # print(max_el)


# nums = [1,2,3,4,23]

# def sq(n):
#     return n * n
# square = map(sq, nums)
# print(list(square))

# result = filter(lambda x: x%2, nums)
# print(list(result))
# result = filter(lambda x: x%2==0, nums)
# print(list(result))


# name = ["Marry", "George", "Elena"]
# age = [24, 30, 22]
# pet = ["cat", "dog", "rabbit"]
# zipped = zip(name, age, pet)
# print(list(zipped))


# # closures

# def num_closure():
    
#     num = []
#     def save_num(num1):
#         num.append(num1)
#         print(num)
#     return save_num
# enter_num = num_closure()
# enter_num(3)
# enter_num(5)


# #Curring
# def change(b, c, d):
#     def a(x):
#         return b(c(d(x)))
#     return a
# def kilometer2meter(dist):
#     return dist * 1000
# def meter2centimeter(dist):
#     return dist * 100
# def centimeters2feet(dist):
#     return dist * 0.032
# transform = change (centimeters2feet, meter2centimeter, kilometer2meter)
# print(transform(300))


# try:
#     a = 5/0 #change 0 with 1 and see results
# except:
#     print("Zero Division!")
# else:
#     print("else")
# finally:
#     print("finally")


# def make_change(func):
#     def inner():
#         print("I got decorated")
#         func()
#         print("over")
#     return inner

# # def ordinary():
# #     print("I'm ordinary!")
# # make_change(ordinary)()

# @make_change
# def ordinary():
#     print("I am ordinary!")
# ordinary()