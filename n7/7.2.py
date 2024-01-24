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