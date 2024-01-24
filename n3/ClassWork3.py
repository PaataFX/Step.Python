######## Cycles ########

# a = 0
# while True:
#     print(a)
#     a = a + 1
#     if a == 11:
#         break
# print("finished")

# for i in range(5):
#     print(i, end=", ")
# # will print: 0, 1, 2, 3, 4, 


# for i in range(2, 5):
#     print(i, end=", ")
# # will print:2, 3, 4, 

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end="\t")
#     print("")
# # 1-100 - multiply table

# i = 0
# while i<11:
#     print(i)
#     i+=1
# # is same as below
# for i in range(11):
#     print(i)

# i = -1
# while i<10:
#     i+=1
#     if (i == 3 or i == 5):
#         continue
#     print(i)

# i = 0
# sum_input = 0
# while i <5:
#     sum_input += int(input("please enter a number: "))
#     i += 1
# print(sum_input, i, end="\t")


# num = int(input("Please enter a number: "))
# even_nums=0
# for i in range(2, num+1, 2):
#     print(i)
#     even_nums += i
# print(even_nums)


# sum_num = 0
# while True:
#     answer = input("Please enter a number (end): ")
#     if answer == "end":
#         break
#     num = int(answer)
#     if num%2 == 0:
#         sum_num += num
# print (sum_num)


# sum_num = 0
# i=0
# while True:
#     answer = input("Please enter a number (end): ")
#     if answer == "end":
#         break
#     num = int(answer)
#     if num%2 == 0:
#         sum_num += num
#         i+=1
# if i!=0:
#     print (sum_num/i)


# x=int(input("enter num"))
# e = 0
# g = x-1
# while True:
#     if e<=x:
#         print("*" * e)
#         e+=1
#     else:
#         print("*" * g)
#         g-=1
#     if g == 0:
#         break




################################################################
# from random import randint

# human_score = 0
# computer_score = 0
# draws = 0

# while (human_score<3) or (computer_score<3):
#     computer_choice = randint(1, 3)
#     human_choice = int(input("""
# Choose a Number: 
# 1. Rock
# 2. Scissors
# 3. Paper
# """))
#     if computer_choice == human_choice:
#         print ("It's a draw!")
#         draws += 1
#     elif (human_choice == 1 and computer_choice == 2) or (human_choice == 2 and computer_choice ==3) or (human_choice == 3 and computer_choice ==1):
#         human_score += 1
#     else:
#         computer_score += 1
#     print (f"""
# Human Score: {human_score}
# Computer Score: {computer_score}
# Number of Draws: {draws}
# """)
#     if computer_score == 3 or human_score == 3:
#         break
# if human_score == 3:
#     print ("Human Wins!")
# elif computer_score == 3:
#     print ("Computer Wins!")
###############################################################


# num = int(input("Number you want for string to go up to"))
# for i in range(num + 1):
#     for j in range(1, i+1):
#         print (j, end=" ")
#     print()