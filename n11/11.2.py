def immutable_set(input_list):
    unique_frozenset = frozenset(input_list)
    return unique_frozenset

user_input = input("Enter a list of elements separated by spaces: ")
input_list = [element.strip() for element in user_input.split()]
result = immutable_set(input_list)
print("Immutable set:", result)
