# შეყვანილი ინფორმაციის გასამმაგება
def triple_and_print(input_str):
    tripled_str = input_str * 3
    print(f"Input: {input_str}\nOutput: Tripled: {tripled_str}")

user_input = input("Enter text: ")

triple_and_print(user_input)

# წონა მთვარეზე
def weight_on_moon(weight_on_earth):
    moon_gravity_ratio = 1 / 6
    weight_on_moon = weight_on_earth * moon_gravity_ratio
    return weight_on_moon

user_weight_earth = float(input("Enter your weight on Earth (in kilograms): "))

user_weight_moon = weight_on_moon(user_weight_earth)

print(f"Your weight on the Moon would be: {user_weight_moon} Kg")

# კალკულატორი
def calculator(expression):
    try:
        num1, operator, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Cannot divide by zero."
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        else:
            return "Error: Invalid operator."

        return result

    except ValueError:
        return "Error: Invalid input. Please enter two numbers and an operator."

user_input = input("Enter an expression (e.g., '2 * 6'): ")

result = calculator(user_input)
print(result)
