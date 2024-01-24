# ჯენერიქ მისალმებას ამრავლებს იმდენჯერ, რა რიცხვსაც მომხმარებელი შეიყვანს და ბეჭდავს
def print_greeting_recursive(n):
    if n > 0:
        print("Hello, User!")
        print_greeting_recursive(n - 1)

try:
    times = int(input("Enter the number of times to print the greeting: "))
    if times < 0:
        print("Please enter a non-negative integer.")
    else:
        print_greeting_recursive(times)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# თავიდან ჩვეულებრივად ავაწყე, მაგრამ შემდეგ ცოტა დავამატე რაღაცები კოდს. კოდი იღებს ინფუთად რაოდენობას და პროდუქტის სახელს (იქნება რაოდენობა სახელის წინ თუ შემდეგ არ აქვს მნიშვნელობა) იქვე წერს იმ შეკვეთას და იმახსოვრებს. როცა მომხარებელი შეიყვანს 'end' დაუბეჭდავს მთლიან შეკვეთას.

def print_order(quantity, dish_name):
    print(f"Order: {quantity} {dish_name}")

orders = []

while True:
    if not orders:
        user_input = input("Enter your order (e.g., '5 burgers' or 'burger 5'): ").lower()
    else:
        user_input = input("Add another dish or type 'end' to finish: ").lower()
    if user_input == 'end':
        break
    try:
        words = user_input.split()
        if words[0].isdigit():
            quantity = int(words[0])
            dish_name = ' '.join(words[1:])
        elif words[-1].isdigit():
            quantity = int(words[-1])
            dish_name = ' '.join(words[:-1])
        else:
            quantity = 1
            dish_name = user_input
        orders.append((quantity, dish_name))
        print("\nCurrent Order:")
        for q, dish in orders:
            print_order(q, dish)
    except ValueError:
        print("Invalid input. Please enter a valid order.")

print("\nYour Final Order:")
for quantity, dish_name in orders:
    print_order(quantity, dish_name)


# მომხმარებელს თავიდან შეყავს, რამდენი რიცხვის გადამრავლება უნდა ერთმანეთზე, შემდეგ სათითაოდ იღებს ამ რიცხვებს და ამრავლებს

def multiply_numbers_from_input():
    try:
        n = int(input("Enter the number of amounts: "))
        if n < 3:
            print("Error: Please provide at least three numbers.")
            return None
        product = 1
        for i in range(n):
            num = float(input(f"Enter number {i + 1}: "))
            product *= num
        print(f"The product of the numbers is: {product}")
        return product
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return None

result = multiply_numbers_from_input()
