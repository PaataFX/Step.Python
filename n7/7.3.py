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
