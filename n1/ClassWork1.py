#a = "treasure"
# address = id(a)
# print (address)
# will print: treasure


# a = "treasure"
# b = "island"
# print(a, b)
# will print: treasure island


# a = "2"
# b = "1"
# print(a+b)
# will print: 21


# a = 2
# b = 1
# print(a+b)
# will print: 3

# Python Arithmetic Operators
# + add
# - subtract
# * multiply
# / division
# % modulus ((11 % 3) Output: 2. because 11 divided by 3 is 3 with a remainder of 2)
# ** exponentiation (ახაისხება)
# // floor division (returns the largest whole number that is less than or equal to the result)


# a = 10.3
# print((type)(a))
# will print: <class 'float'>
# print((type)(x)) is for identification purposes of x. what kind of data type is it

# types of Data
# Text Type:        str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type: 	dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType


# a = 10.3
# print(int(a))
# will print: 10
# (int) turned it into integer


# a = 1
# b = 2
# print(a, b, sep="\n")
# will print: 1 \n 2 on separate lines


# a = input("input your name: ")
# print (a)
# will print: what you'll input in a string!!!


# a = int(input("input number: "))
# print (a)
# will print number as you give turned intu integer!!!
# if you type string type data in it and turn into integer, it'll be error.


# user = input("Enter User Name: ")
# pas = input("Enter Password: ")
# length = len(pas)
# print(f"""
# Username: {user}
# Password: {pas}
# Password Length: {length}
# """)


# user = input("Enter User Name: ")
# pas = input("Enter Password: ")
# length = len(pas)
# print("""
# Username: {2}
# Password: {0}
# Password Length: {1}
# """.format(pas, length, user))