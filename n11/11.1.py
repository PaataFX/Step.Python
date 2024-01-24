def unique_list(input_list):
    unique_set = set(input_list)
    unique_list_result = list(unique_set)
    return unique_list_result

user_input = input("Enter a list of numbers separated by spaces: ")
input_list = [int(num) for num in user_input.split()]
result = unique_list(input_list)
print("Unique list:", result)
