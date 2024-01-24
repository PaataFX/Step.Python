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