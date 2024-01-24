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
