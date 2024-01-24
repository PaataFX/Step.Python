multiply_by = lambda x, multiplier: list(map(lambda y: y * multiplier, x))

input_list_str = input("Enter a list of numbers separated by spaces: ")
input_list = [float(item) for item in input_list_str.split()]

multiplier = float(input("Enter the multiplier: "))

result_list = multiply_by(input_list, multiplier)

print(f"Original List: {input_list}")
print(f"Multiplier: {multiplier}")
print(f"Result List: {result_list}")
