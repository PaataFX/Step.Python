def set_to_tuple(set1, set2):
    combined_set = set1.union(set2)
    result_tuple = tuple(combined_set)
    return result_tuple

input_set1 = set(input("Enter elements for the first set separated by spaces: ").split())
input_set2 = set(input("Enter elements for the second set separated by spaces: ").split())

result = set_to_tuple(input_set1, input_set2)
print("Resulting tuple:", result)
