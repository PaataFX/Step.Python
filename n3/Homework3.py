# ჯეირანის პროგრამა

import random

human_point = 0
comp_point = 0

while True:
    human_choice = int(input('''
    choose:
    1. rock
    2. scissors
    3. paper
    input the number (1-3): 
    '''))
    
    computer_choice = random.randint(1, 3)
    
    print(f'score: {human_point} : {comp_point}')
    
    if human_point != 3 and comp_point != 3:
        if human_choice == computer_choice:
            print("It's a tie!")
        elif (human_choice == 1 and computer_choice == 2) or (human_choice == 2 and computer_choice == 3) or (human_choice == 3 and computer_choice == 1):
            print('You win this round!')
            human_point += 1
        else:
            print('Computer wins this round!')
            comp_point += 1
    elif human_point == 3:
        print('You Won!')
        break
    else:
        print('You Lost!')
        break

# გამრავლების ტაბულა

n = int(input("Choose the number you want for multiply to: "))
n += 1
for i in range(1, n):
    for j in range(1, n):
        result = i * j
        print(result, end="\t")
    print()

# საბანკო ანგარიში

acount = int(3000)

while True:
    if acount == 0:
        break
    elif acount >= 0 :
        expense = int(input("enter your expenses: "))
        if expense <= acount:
            acount -= expense
        elif expense >= acount:
            print ("You have not enough money to spend")
        print(f"your balance is {acount}")
        continue

# თუთიყუში

while True:
    parrot = input("User Said Whaaat!? ")
    print ("user said whaaat!?", f"User Said {parrot}", sep='\n')
    if parrot.lower() == "quit":
        break
    else:
        continue
