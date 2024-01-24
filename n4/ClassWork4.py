############ String Methods: #################################
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()        	Searches the string for a specified value and returns the position of where it was found
# format()      	Formats specified values in a string
# format_map()  	Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()         Returns True if all characters in the string are alphanumeric
# isalpha()     	Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()   	Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning

################################################################################################

# regular expressions
# Character	                    Description	                                                Example
# []	    A set of characters	                                                            "[a-m]"	
# \	        Signals a special sequence (can also be used to escape special characters)	    "\d"	
# .	        Any character (except newline character)	                                    "he..o"	
# ^	        Starts with	                                                                    "^hello"	
# $	        Ends with	                                                                    "planet$"	
# *	        Zero or more occurrences	                                                    "he.*o"	
# +	        One or more occurrences	                                                        "he.+o"	
# ?	        Zero or one occurrences                                                     	"he.?o"	
# {}	    Exactly the specified number of occurrences	                                    "he.{2}o"	
# |	        Either or	                                                                    "falls|stays"

# word = input("type something: ")
# print(word[2])

# word = input("type something: ")
# print(word[-5])

# word = input("type something: ")
# print(word[1:3])

# word = input("type something: ")
# print(word[:3])

# word = input("type something: ")
# print(word[1:])

# word = input("type something: ")
# print(word[1:7:2])
# # from 2 to 7 it takes every second symbol

# word = input("type something: ")
# for i in word:
#     print(i)
######## is same as
# word = input("type something: ")
# index = 0
# while index < len(word):
#     print(word[index])
#     index += 1

# user = input("Enter username: ").strip()
# pas = input("Enter password: ").strip()
# if (user == "user2023") and (pas == "pas2023"):
#     print("correct!")  

# word = "Hello everyone, I am Groot!"
# print(word.replace("Groot", "Batman" ))
# print(word)
# # .replace doesn't change a string, it just replaces a word. if we want it changed we need to use word = .replace and so on

# word = "Hello \"everyone\", I am Groot!"
# print(word)

# import re
# sentence = input("Enter sentence: ")
# answer = re.search('^the.*spain$', sentence)
# if answer:
#     print("yes")
# else:
#     print("no")

# import re
# sentence = input("Enter sentence: ")
# answer = re.findall('USA', sentence)
# if len(answer)>0:
#     print("yes")
# else:
#     print("no")


# sentence = input("Enter sentence: ")
# print(sentence.split())
# # is the same as
# import re
# sentence = input("Enter sentence: ")
# answer = re.split("\s", sentence)
# print(answer)

# import re
# sentence = input("Enter sentence: ")
# print(sentence.isalpha())
# print(sentence.isdigit())


# import random
# data = ["paper", "scissors", "stone"]
# human_score = 0
# comp_score = 0
# while human_score <3 and comp_score <3:
#     human_choice = input("enter your choice (paper, scissors, stone): ").lower().strip()
#     if human_choice not in data:
#         continue
#     else:
#         comp_choice = random.choice(data)
        
#         human_win = (human_choice == "paper" and comp_choice == "stone") or (human_choice == "stone" and comp_choice == "scissors") or (human_choice == "scissors" and comp_choice == "paper")
        
#         if human_choice == comp_choice:
#             print ("Draw!")
#             continue
#         elif human_win:
#             print("Human +1")
#             human_score += 1
#         else:
#             print("Comp +1")
#             comp_score += 1
# print(f"""
# Human Score: {human_score}
# Comp Score: {comp_score}
# """)