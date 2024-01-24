import random

human_point = 0
comp_point = 0

while True:
    human_choice = int(input('''
    choose a number:
    1. rock
    2. scissors
    3. paper
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
