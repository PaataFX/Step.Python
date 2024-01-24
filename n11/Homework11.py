# დავალებამ ცოტა დამაბნია და იმედია, სწორად შევასრულე.
def unique_list(input_list):
    unique_set = set(input_list)
    unique_list_result = list(unique_set)
    return unique_list_result

user_input = input("Enter a list of numbers separated by spaces: ")
input_list = [int(num) for num in user_input.split()]
result = unique_list(input_list)
print("Unique list:", result)

# 

def immutable_set(input_list):
    unique_frozenset = frozenset(input_list)
    return unique_frozenset

user_input = input("Enter a list of elements separated by spaces: ")
input_list = [element.strip() for element in user_input.split()]
result = immutable_set(input_list)
print("Immutable set:", result)


# 

def set_to_tuple(set1, set2):
    combined_set = set1.union(set2)
    result_tuple = tuple(combined_set)
    return result_tuple

input_set1 = set(input("Enter elements for the first set separated by spaces: ").split())
input_set2 = set(input("Enter elements for the second set separated by spaces: ").split())

result = set_to_tuple(input_set1, input_set2)
print("Resulting tuple:", result)