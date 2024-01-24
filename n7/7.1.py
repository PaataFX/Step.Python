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

